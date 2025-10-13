#!/usr/bin/env python3
"""
Coffee Bar Connoisseur - Zapier Webhook for Social Media Automation
This script creates a webhook endpoint to trigger social media posts
when playlists are updated.
"""

from flask import Flask, request, jsonify
import requests
import json
from datetime import datetime
import os

app = Flask(__name__)

# Zapier Webhook URLs (you'll get these from your Zapier Zaps)
ZAPIER_WEBHOOKS = {
    'facebook': os.getenv('ZAPIER_FACEBOOK_WEBHOOK_URL', ''),
    'instagram': os.getenv('ZAPIER_INSTAGRAM_WEBHOOK_URL', ''),
    'threads': os.getenv('ZAPIER_THREADS_WEBHOOK_URL', ''),
    'youtube': os.getenv('ZAPIER_YOUTUBE_WEBHOOK_URL', ''),
    'general': os.getenv('ZAPIER_GENERAL_WEBHOOK_URL', '')
}

# Playlist information
PLAYLISTS = {
    '4qPIPw6PIfUFIpsoFrAIlQ': 'Sundown Vibes: Afrobeat',
    '1EaQK9jmCLaYt4kUwXzyei': '5HR Energy Drill Party',
    '6mpnPV8vQlyPAJ8mgrB3Cm': 'DJmix: Ultimate Party',
    '2S676Ysy6lBZkYqdHFYQoQ': 'HITS: Women Front & Center',
    '1hKhrLHN4WliXFzH2DuAjB': 'MorningBrew Bossa Nova Chill',
    '3WC0mTKjR0Q8HdAnYP5zCt': 'MorningBrew Jazz Classics LOFI',
    '5W7z4W93kHJU8HIgYxYU0J': 'Sundown Vibes | Rap Reggae 10 HR BLISS',
    '7sU1PGsAAmF5y7bW6tAPsY': 'Spotify Chart Toppers - Gym, Coffee, likes'
}

def create_social_media_content(playlist_id, playlist_name, update_type="weekly"):
    """Generate social media content for playlist updates"""
    
    # Coffee Bar Connoisseur branding
    brand_hashtags = "#CoffeeBarConnoisseur #RueDeVivre #CuratedVibes"
    
    # Playlist-specific hashtags
    playlist_tags = {
        '4qPIPw6PIfUFIpsoFrAIlQ': "#Afrobeat #SundownVibes #GoldenHour",
        '1EaQK9jmCLaYt4kUwXzyei': "#DrillParty #EnergyBoost #HighVibe",
        '6mpnPV8vQlyPAJ8mgrB3Cm': "#UltimateParty #DJMix #FestivalVibes",
        '2S676Ysy6lBZkYqdHFYQoQ': "#WomenInMusic #Hits #Empowerment",
        '1hKhrLHN4WliXFzH2DuAjB': "#BossaNova #MorningBrew #ChillVibes",
        '3WC0mTKjR0Q8HdAnYP5zCt': "#JazzClassics #Lofi #CoffeeShopVibes",
        '5W7z4W93kHJU8HIgYxYU0J': "#RapReggae #10HourBliss #Sundown",
        '7sU1PGsAAmF5y7bW6tAPsY': "#ChartToppers #GymMusic #CoffeeTime"
    }
    
    playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
    website_url = "https://coffeebarconnoisseur.com"  # Update with your actual domain
    
    content = {
        'text': f"""🎵 Fresh vibes brewing! ☕️

{playlist_name} has been updated with new tracks to match your energy!

Stream the perfect soundtrack for your coffee moments: {playlist_url}

{playlist_tags.get(playlist_id, "#MusicDiscovery #CoffeeCulture")}
{brand_hashtags}

#CoffeeAndMusic #PlaylistUpdate #WeeklyVibes""",
        
        'image_url': 'https://coffeebarconnoisseur.com/coffee_connoisseur_matisse.png',
        'link_url': playlist_url,
        'link_title': f'{playlist_name} - Coffee Bar Connoisseur',
        'link_description': 'Curated playlists brewed to match your energy'
    }
    
    return content

def send_to_zapier(platform, content):
    """Send content to Zapier webhook for specific platform"""
    webhook_url = ZAPIER_WEBHOOKS.get(platform)
    
    if not webhook_url:
        print(f"No webhook URL configured for {platform}")
        return False
    
    try:
        response = requests.post(
            webhook_url,
            json={
                'platform': platform,
                'content': content,
                'timestamp': datetime.now().isoformat(),
                'brand': 'Coffee Bar Connoisseur'
            },
            timeout=30
        )
        
        if response.status_code == 200:
            print(f"Successfully sent to {platform}")
            return True
        else:
            print(f"Failed to send to {platform}: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Error sending to {platform}: {str(e)}")
        return False

@app.route('/webhook/playlist-update', methods=['POST'])
def playlist_update_webhook():
    """Webhook endpoint for playlist updates"""
    try:
        data = request.get_json()
        
        playlist_id = data.get('playlist_id')
        playlist_name = data.get('playlist_name', PLAYLISTS.get(playlist_id, 'Unknown Playlist'))
        update_type = data.get('update_type', 'weekly')
        
        # Create social media content
        content = create_social_media_content(playlist_id, playlist_name, update_type)
        
        # Send to all platforms
        results = {}
        for platform in ['facebook', 'instagram', 'threads', 'youtube']:
            results[platform] = send_to_zapier(platform, content)
        
        return jsonify({
            'status': 'success',
            'message': 'Social media posts triggered',
            'playlist': playlist_name,
            'platforms': results
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/webhook/weekly-update', methods=['POST'])
def weekly_update_webhook():
    """Webhook for weekly scheduled updates"""
    try:
        data = request.get_json()
        featured_playlist = data.get('featured_playlist', '4qPIPw6PIfUFIpsoFrAIlQ')
        playlist_name = PLAYLISTS.get(featured_playlist, 'Featured Playlist')
        
        content = create_social_media_content(featured_playlist, playlist_name, 'weekly')
        
        # Send to all platforms
        results = {}
        for platform in ['facebook', 'instagram', 'threads', 'youtube']:
            results[platform] = send_to_zapier(platform, content)
        
        return jsonify({
            'status': 'success',
            'message': 'Weekly social media posts triggered',
            'featured_playlist': playlist_name,
            'platforms': results
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Coffee Bar Connoisseur Webhook',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🎵 Coffee Bar Connoisseur Webhook Server Starting...")
    print("📱 Social Media Automation Ready!")
    print("🔗 Webhook endpoints:")
    print("   POST /webhook/playlist-update")
    print("   POST /webhook/weekly-update")
    print("   GET /health")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
