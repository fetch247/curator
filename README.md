# 🎵 Coffee Bar Connoisseur - High Vibe Edition

A sleek, millennial-friendly website showcasing curated Spotify playlists with glassmorphism design and festival lounge aesthetics.

## 🚀 Features

- **Modern Design**: Glassmorphism effects with neon glow and smooth animations
- **8 Curated Playlists**: From afrobeat to drill party, jazz classics to chart toppers
- **Responsive Layout**: Two-column design with featured playlists and rotating carousel
- **Social Media Integration**: Automated Wednesday posting via Zapier
- **Spotify Integration**: Direct embeds and links to all playlists

## 📱 Social Media Automation

### Zapier Setup (Wednesday Posts)

1. **GitHub Actions**: Automatically triggers every Wednesday at 9 AM UTC
2. **Playlist Rotation**: Cycles through all 8 playlists weekly
3. **Multi-Platform**: Posts to Facebook, Instagram, Threads, and YouTube
4. **Smart Content**: Auto-generates hashtags and descriptions for each playlist

### Required Setup:

1. **Add Zapier Webhook URL** to GitHub Secrets:
   - Go to your GitHub repository
   - Settings → Secrets and variables → Actions
   - Add secret: `ZAPIER_WEBHOOK_URL` with your Zapier webhook URL

2. **Configure Zapier Zap**:
   - Trigger: Webhooks by Zapier
   - Action: Facebook Pages (and other platforms)
   - Connect your webhook URL from GitHub Actions

## 🎵 Playlists

### Featured (Left Side):
- **Sundown Vibes: Afrobeat** - Golden hour energy with smooth afrobeat rhythms
- **5HR Energy Drill Party** - High-octane drill beats to fuel your energy  
- **DJmix: Ultimate Party** - The ultimate party mix for maximum energy

### Rotating Carousel (Right Side):
- **HITS: Women Front & Center** - Celebrating incredible female artists
- **MorningBrew Bossa Nova Chill** - Smooth bossa nova vibes
- **MorningBrew Jazz Classics LOFI** - Classic jazz with modern lofi production
- **Sundown Vibes | Rap Reggae 10 HR BLISS** - Extended rap and reggae
- **Spotify Chart Toppers** - Current hits for workouts and coffee

## 🛠️ Technical Stack

- **HTML5** with modern CSS (Grid, Flexbox, CSS Variables)
- **JavaScript** for animations and interactions
- **GitHub Actions** for automation
- **Zapier** for social media posting
- **Spotify API** integration

## 📁 File Structure

```
├── index.html                    # Main website
├── zapier-config.json           # Playlist configuration for Zapier
├── .github/workflows/           # GitHub Actions automation
│   └── weekly-social-media.yml  # Wednesday posting workflow
├── requirements-webhook.txt     # Python dependencies (optional)
├── zapier-webhook.py           # Webhook server (optional)
└── ZAPIER_SETUP_GUIDE.md       # Detailed setup instructions
```

## 🎨 Design Features

- **Glassmorphism**: Semi-transparent cards with backdrop blur
- **Neon Aesthetics**: Glowing text and hover effects
- **Smooth Animations**: Fade-in, hover, and parallax effects
- **Color-Coded Playlists**: Each playlist type has unique accent colors
- **Responsive Grid**: Adapts beautifully to all screen sizes

## 🔧 Local Development

1. **Clone the repository**
2. **Open `index.html`** in your browser
3. **For webhook server** (optional):
   ```bash
   pip install -r requirements-webhook.txt
   python zapier-webhook.py
   ```

## 📊 Analytics & Monitoring

- **GitHub Actions logs** show automation status
- **Zapier dashboard** tracks social media post success
- **Spotify analytics** available in your Spotify for Artists dashboard

## 🌟 Branding

- **Coffee Bar Connoisseur** - Main brand
- **Rue de Vivre** - Music production
- **High Vibe Edition** - Design theme
- **Festival lounge meets modern streaming app** - Aesthetic

## 📞 Support

For questions about the automation or setup:
- Check the `ZAPIER_SETUP_GUIDE.md` for detailed instructions
- Review GitHub Actions logs for automation status
- Monitor Zapier dashboard for social media posting

---

**Ready to brew some high vibes? Your Coffee Bar Connoisseur is now fully automated! ☕️🎵**
