import requests

url = "${{ secrets.JU }}"
response = requests.get(url)
data = response.json()

max_items = 10
svg_height = 940

svg_content = f'''
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="800" height="{svg_height}">
  <foreignObject width="800" height="{svg_height}">
    <div xmlns="http://www.w3.org/1999/xhtml" class="container">
      <style>
        /* CSS Reset */
        html, body, div, span, h1, p {{ margin: 0; padding: 0; border: 0; font-size: 100%; font: inherit; vertical-align: baseline; }}
        /* Container Style */
        .container {{
          font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif;
          padding: 20px; /* Pastikan padding cukup untuk mencegah pemotongan */
          border-radius: 10px; /* Sudut membulat */
          background-color: #212121;
          color: #FFFFFF;
          width: 100%;
          height: 100%;
          display: flex;
          flex-direction: column;
          gap: 20px;
          border: 2px solid #444;  /* Border untuk kontainer */
          box-sizing: border-box; /* Mengatur box-sizing untuk mencegah pemotongan */
        }}
        .title {{
          font-size: 24px;
          font-weight: bold;
          text-align: center;
          margin-bottom: 20px;
        }}
        .movie-item {{
          display: flex;
          flex-direction: column;
          gap: 5px;
          border-bottom: 1px solid #444;
          padding-bottom: 10px;
        }}
        .movie-title {{
          font-size: 18px;
          font-weight: bold;
          color: #FFFFFF;
        }}
        .movie-year {{
          font-size: 14px;
          font-style: italic;
          color: #AAAAAA;
        }}
        .watched-at {{
          font-size: 14px;
          color: #888888;
          margin-top: 5px;  /* Tambahkan margin untuk spasi yang lebih baik */
          white-space: nowrap; /* Mencegah pemisahan baris */
        }}
      </style>
      <div class="container">
        <div class="title">Recently Watched Movies</div>
'''

for i, item in enumerate(data):
    if i >= max_items:  
      break
    
    title = item['movie']['title']
    year = item['movie']['year']
    watched_at = item['watched_at']
  
    title = title.replace('&', 'and')
    
    watched_date, watched_time = watched_at.split("T")  # Pisahkan tanggal dan waktu
    watched_date = watched_date.replace("-", "/")  # Ganti '-' dengan '/' untuk tampilan yang lebih bersih
    
    watched_time = watched_time.split(":")[:2]  # Ambil jam dan menit
    watched_time = ":".join(watched_time)  # Gabungkan kembali menjadi string

    watched_at_formatted = f"Watched on: {watched_date} at {watched_time} UTC"

    svg_content += f'''
        <div class="movie-item">
          <span class="movie-title">{title} ({year})</span>
          <span class="watched-at">{watched_at_formatted}</span>
        </div>
    '''


svg_content += '''
      </div>
    </div>
  </foreignObject>
</svg>
'''

with open("profile.svg", "w") as file:
    file.write(svg_content)

print("SVGs have been created and saved as thm.svg.")
