# CloudFlare Tunnel
Make your localhost server as a website / API server & more. You may check the [documentation](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) for more details.

## Setup CloudFlare
Sign-up [here](https://dash.cloudflare.com/) & you do not even need a credit card. Then follow the steps as shown in the video.

## Configurations on Android
You can use `Termux` or `Wayland` or some similar terminal on your android. I am going to use Termux.

### Temux Setup

1. Install Termux from GutHub / F-Droid / PlayStore.

2. Install `Python` (or whatever backend technology you use) & `cloudflared` agent.
```bash
pkg install python
pkg install cloudflared
```

3. Install `flask` (I have used this on python)
```bash
pip install flask # virtual env is recommended
```

4. Then use this [sample code](./app.py) to run your server.
```bash
python app.py
```

5. Run the cloudflare service or run cloudflare manually as show on the cloudflare console.
