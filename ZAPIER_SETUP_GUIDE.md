# 🎵 Coffee Bar Connoisseur - Zapier Social Media Automation Setup

## Overview
This guide will help you set up automated social media posting for your Coffee Bar Connoisseur playlists across Facebook, Instagram, Threads, and YouTube using Zapier.

## 🚀 Quick Setup (Recommended: Weekly Scheduled Posts)

### Step 1: Create Your Zapier Zaps

#### **Zap 1: Facebook Page Post**
1. **Trigger:** Schedule by Zapier
   - Frequency: Weekly
   - Day: Monday
   - Time: 9:00 AM (your timezone)
   
2. **Action:** Facebook Pages
   - Action: Create Page Post
   - Page: Select your Coffee Bar Connoisseur page
   - Message: Use this template:
   ```
   🎵 Fresh vibes brewing! ☕️
   
   {Featured Playlist Name} has been updated with new tracks to match your energy!
   
   Stream the perfect soundtrack for your coffee moments: {Spotify Link}
   
   {Playlist-specific hashtags}
   #CoffeeBarConnoisseur #RueDeVivre #CuratedVibes
   #CoffeeAndMusic #PlaylistUpdate #WeeklyVibes
   ```

#### **Zap 2: Instagram Post**
1. **Trigger:** Schedule by Zapier (same as Facebook)
2. **Action:** Instagram
   - Action: Create Photo Post
   - Image: Upload your Coffee Bar Connoisseur logo
   - Caption: Same template as Facebook

#### **Zap 3: Threads Post**
1. **Trigger:** Schedule by Zapier (same as others)
2. **Action:** Meta Threads
   - Action: Create Thread
   - Text: Same template as Facebook

#### **Zap 4: YouTube Community Post**
1. **Trigger:** Schedule by Zapier (same as others)
2. **Action:** YouTube
   - Action: Create Community Post
   - Text: Same template as Facebook

### Step 2: Create Multiple Zaps for Different Playlists

Create separate Zaps for each of your main playlists:
- **Sundown Vibes AFROBEAT** (Mondays)
- **5HR Energy Drill Party** (Wednesdays)  
- **DJmix-UltimatePARTY** (Fridays)
- **MorningBrew Series** (Tuesdays/Thursdays)

## 🔧 Advanced Setup (Webhook-Based)

### Step 1: Deploy the Webhook Server

1. **Install dependencies:**
   ```bash
   pip install -r requirements-webhook.txt
   ```

2. **Set environment variables:**
   ```bash
   export ZAPIER_FACEBOOK_WEBHOOK_URL="https://hooks.zapier.com/hooks/catch/YOUR_FACEBOOK_WEBHOOK_ID"
   export ZAPIER_INSTAGRAM_WEBHOOK_URL="https://hooks.zapier.com/hooks/catch/YOUR_INSTAGRAM_WEBHOOK_ID"
   export ZAPIER_THREADS_WEBHOOK_URL="https://hooks.zapier.com/hooks/catch/YOUR_THREADS_WEBHOOK_ID"
   export ZAPIER_YOUTUBE_WEBHOOK_URL="https://hooks.zapier.com/hooks/catch/YOUR_YOUTUBE_WEBHOOK_ID"
   ```

3. **Run the webhook server:**
   ```bash
   python zapier-webhook.py
   ```

### Step 2: Create Webhook-Triggered Zaps

For each platform, create a Zap with:
1. **Trigger:** Webhooks by Zapier
2. **Action:** Your social media platform
3. **Copy the webhook URL** and add it to your environment variables

### Step 3: Test the Webhook

Send a test request:
```bash
curl -X POST http://localhost:5000/webhook/weekly-update \
  -H "Content-Type: application/json" \
  -d '{"featured_playlist": "4qPIPw6PIfUFIpsoFrAIlQ"}'
```

## 📱 Social Media Templates

### **Weekly Update Template:**
```
🎵 Fresh vibes brewing! ☕️

{Playlist Name} has been updated with new tracks to match your energy!

Stream the perfect soundtrack for your coffee moments: {Spotify Link}

{Playlist-specific hashtags}
#CoffeeBarConnoisseur #RueDeVivre #CuratedVibes
#CoffeeAndMusic #PlaylistUpdate #WeeklyVibes
```

### **Playlist-Specific Hashtags:**
- **Sundown Vibes:** #Afrobeat #SundownVibes #GoldenHour
- **Energy Drill:** #DrillParty #EnergyBoost #HighVibe  
- **Ultimate Party:** #UltimateParty #DJMix #FestivalVibes
- **Women Front:** #WomenInMusic #Hits #Empowerment
- **MorningBrew:** #BossaNova #MorningBrew #ChillVibes
- **Jazz Classics:** #JazzClassics #Lofi #CoffeeShopVibes

## 🎯 Best Practices

### **Posting Schedule:**
- **Monday:** Sundown Vibes (perfect for week start)
- **Tuesday:** MorningBrew Bossa Nova (midweek chill)
- **Wednesday:** 5HR Energy Drill (hump day boost)
- **Thursday:** Jazz Classics LOFI (coffee shop vibes)
- **Friday:** Ultimate Party (weekend energy)

### **Content Variations:**
- Rotate between different playlists each week
- Include seasonal themes (holiday music, summer vibes, etc.)
- Share behind-the-scenes coffee brewing content
- Feature specific artists or tracks

### **Engagement Tips:**
- Ask followers to share their favorite coffee + music combinations
- Create polls about which playlist they're listening to
- Share coffee brewing tips with playlist recommendations
- Respond to comments to build community

## 🔗 Integration with Your Website

Add this to your HTML to trigger social media posts:

```javascript
// Add to your website's JavaScript
function triggerSocialMediaUpdate(playlistId) {
    fetch('/webhook/playlist-update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            playlist_id: playlistId,
            update_type: 'manual'
        })
    });
}
```

## 📊 Analytics & Monitoring

### **Track Performance:**
- Monitor engagement rates on each platform
- Track click-through rates to Spotify playlists
- Measure follower growth after implementing automation
- A/B test different posting times and content

### **Zapier Analytics:**
- Check Zap success rates in Zapier dashboard
- Set up email notifications for failed Zaps
- Monitor webhook usage and limits

## 🚨 Troubleshooting

### **Common Issues:**
1. **Zaps not triggering:** Check timezone settings
2. **Posts not appearing:** Verify social media app permissions
3. **Webhook errors:** Check server logs and Zapier webhook status
4. **Rate limits:** Spread posts across different times/days

### **Support Resources:**
- Zapier Help Center
- Facebook Business Help
- Instagram Creator Help
- YouTube Creator Support

## 💡 Pro Tips

1. **Create a content calendar** to plan weekly themes
2. **Use Zapier's filters** to customize posts for different platforms
3. **Set up backup Zaps** in case primary ones fail
4. **Monitor trending hashtags** and incorporate them
5. **Engage with your audience** by responding to comments
6. **Cross-promote** between your website and social media

---

**Ready to automate your Coffee Bar Connoisseur social media presence? Start with the weekly scheduled posts for the most reliable results!** ☕️🎵
