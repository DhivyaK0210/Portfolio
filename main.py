from pathlib import Path
import zipfile, shutil, textwrap

out = Path("/mnt/data/burgundy_portfolio_with_ai_photo")
out.mkdir(exist_ok=True)

ai_src = Path("/mnt/data/a_vibrant_futuristic_outdoor_portrait_scene_wide.png")
ai_name = "dhivya-ai-tech.png"
if ai_src.exists():
    shutil.copy(ai_src, out / ai_name)

profile_src = Path("/mnt/data/Profile.pdf")
if profile_src.exists():
    shutil.copy(profile_src, out / "Profile.pdf")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Dhivyadharshini Karunakaran | Portfolio</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet">

  <style>
    :root {{
      --burgundy: #641220;
      --wine: #8a1538;
      --rose: #b23a48;
      --cream: #fff3df;
      --cream-light: #fffaf0;
      --gold: #d4a373;
      --ink: #291417;
      --muted: #7b5f58;
      --shadow: 0 22px 55px rgba(100, 18, 32, .18);
      --radius: 30px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: Inter, sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 15% 8%, rgba(178, 58, 72, .22), transparent 26%),
        radial-gradient(circle at 90% 18%, rgba(212, 163, 115, .35), transparent 24%),
        radial-gradient(circle at 25% 85%, rgba(100, 18, 32, .18), transparent 28%),
        var(--cream);
      overflow-x: hidden;
    }}

    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(100, 18, 32, .05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(100, 18, 32, .05) 1px, transparent 1px);
      background-size: 38px 38px;
      pointer-events: none;
      z-index: -1;
    }}

    .container {{
      width: min(1120px, 92%);
      margin: auto;
    }}

    header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 243, 223, .78);
      backdrop-filter: blur(20px);
      border-bottom: 1px solid rgba(100, 18, 32, .12);
    }}

    nav {{
      height: 76px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .logo {{
      font-family: "Space Grotesk", sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--burgundy);
      text-decoration: none;
    }}

    .logo span {{
      display: inline-block;
      background: var(--burgundy);
      color: var(--cream);
      padding: .25rem .55rem;
      border-radius: 12px;
      transform: rotate(-3deg);
      margin-right: .3rem;
    }}

    .nav-links {{
      display: flex;
      gap: 1.2rem;
      list-style: none;
    }}

    .nav-links a {{
      color: var(--ink);
      text-decoration: none;
      font-weight: 700;
      font-size: .93rem;
    }}

    .nav-links a:hover {{
      color: var(--wine);
    }}

    .hero {{
      min-height: calc(100vh - 76px);
      display: grid;
      grid-template-columns: 1.05fr .95fr;
      align-items: center;
      gap: 3rem;
      padding: 4rem 0;
    }}

    .eyebrow {{
      display: inline-flex;
      gap: .55rem;
      align-items: center;
      background: var(--burgundy);
      color: var(--cream);
      padding: .7rem 1rem;
      border-radius: 999px;
      font-weight: 800;
      box-shadow: var(--shadow);
      margin-bottom: 1.2rem;
    }}

    h1 {{
      font-family: "Space Grotesk", sans-serif;
      font-size: clamp(3rem, 7vw, 6.2rem);
      line-height: .88;
      letter-spacing: -3px;
      color: var(--burgundy);
      margin-bottom: 1.3rem;
    }}

    h1 .cream-tag {{
      display: inline-block;
      color: var(--cream);
      background: linear-gradient(135deg, var(--wine), var(--rose));
      border-radius: 26px;
      padding: .1em .18em .16em;
      transform: rotate(-2deg);
      box-shadow: var(--shadow);
    }}

    .hero-text {{
      color: var(--muted);
      font-size: 1.1rem;
      line-height: 1.8;
      max-width: 650px;
      margin-bottom: 1.6rem;
    }}

    .cta-row {{
      display: flex;
      gap: 1rem;
      flex-wrap: wrap;
      margin-bottom: 2rem;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: .55rem;
      padding: 1rem 1.25rem;
      border-radius: 999px;
      text-decoration: none;
      font-weight: 900;
      transition: .25s;
    }}

    .btn.primary {{
      background: var(--burgundy);
      color: var(--cream);
      box-shadow: var(--shadow);
    }}

    .btn.secondary {{
      background: var(--cream-light);
      color: var(--burgundy);
      border: 2px solid rgba(100, 18, 32, .14);
    }}

    .btn:hover {{
      transform: translateY(-4px);
    }}

    .mini-stats {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      max-width: 620px;
    }}

    .stat {{
      background: rgba(255, 250, 240, .88);
      border: 1px solid rgba(100, 18, 32, .12);
      border-radius: 24px;
      padding: 1rem;
      box-shadow: 0 12px 30px rgba(100, 18, 32, .08);
    }}

    .stat strong {{
      font-family: "Space Grotesk", sans-serif;
      font-size: 1.75rem;
      color: var(--wine);
      display: block;
    }}

    .stat span {{
      color: var(--muted);
      font-size: .88rem;
      font-weight: 700;
    }}

    .photo-card {{
      position: relative;
      background: var(--burgundy);
      border-radius: 44px;
      padding: 1.1rem;
      box-shadow: var(--shadow);
      transform: rotate(2deg);
    }}

    .photo-card img {{
      width: 100%;
      min-height: 520px;
      max-height: 650px;
      object-fit: cover;
      border-radius: 34px;
      display: block;
      border: 2px solid rgba(255, 243, 223, .35);
    }}

    .sticker {{
      position: absolute;
      top: 34px;
      right: -16px;
      background: var(--gold);
      color: var(--burgundy);
      font-weight: 900;
      padding: .9rem 1.1rem;
      border-radius: 18px;
      box-shadow: var(--shadow);
      transform: rotate(8deg);
      z-index: 2;
    }}

    .photo-caption {{
      position: absolute;
      left: 28px;
      bottom: 28px;
      right: 28px;
      padding: 1rem;
      border-radius: 22px;
      background: rgba(100, 18, 32, .78);
      color: var(--cream);
      backdrop-filter: blur(8px);
    }}

    .photo-caption h2 {{
      font-family: "Space Grotesk", sans-serif;
      font-size: 1.6rem;
      margin-bottom: .2rem;
    }}

    section {{
      padding: 5rem 0;
    }}

    .section-head {{
      text-align: center;
      margin-bottom: 2.4rem;
    }}

    .section-head h2 {{
      font-family: "Space Grotesk", sans-serif;
      font-size: 2.55rem;
      color: var(--burgundy);
      margin-bottom: .4rem;
    }}

    .section-head p {{
      color: var(--muted);
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.2rem;
    }}

    .card {{
      background: rgba(255, 250, 240, .9);
      border: 1px solid rgba(100, 18, 32, .12);
      border-radius: var(--radius);
      padding: 1.45rem;
      box-shadow: 0 16px 38px rgba(100, 18, 32, .10);
      transition: .25s;
      position: relative;
      overflow: hidden;
    }}

    .card::after {{
      content: "";
      position: absolute;
      width: 110px;
      height: 110px;
      background: rgba(178, 58, 72, .08);
      border-radius: 999px;
      right: -35px;
      top: -35px;
    }}

    .card:hover {{
      transform: translateY(-8px) rotate(-1deg);
    }}

    .icon {{
      width: 52px;
      height: 52px;
      border-radius: 17px;
      display: grid;
      place-items: center;
      background: var(--burgundy);
      color: var(--cream);
      font-size: 1.6rem;
      margin-bottom: 1rem;
    }}

    .card h3 {{
      font-family: "Space Grotesk", sans-serif;
      color: var(--burgundy);
      margin-bottom: .55rem;
      font-size: 1.25rem;
    }}

    .card p {{
      color: var(--muted);
      line-height: 1.7;
      font-size: .95rem;
    }}

    .skills-wrap {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: .8rem;
    }}

    .skill {{
      background: var(--burgundy);
      color: var(--cream);
      padding: .8rem 1rem;
      border-radius: 999px;
      font-weight: 900;
      box-shadow: 0 10px 24px rgba(100, 18, 32, .14);
    }}

    .skill:nth-child(even) {{
      background: var(--cream-light);
      color: var(--burgundy);
      border: 2px solid rgba(100, 18, 32, .14);
    }}

    .timeline {{
      display: grid;
      gap: 1rem;
      max-width: 900px;
      margin: auto;
    }}

    .timeline-item {{
      display: grid;
      grid-template-columns: 190px 1fr;
      gap: 1rem;
      align-items: start;
      background: rgba(255, 250, 240, .9);
      border: 1px solid rgba(100, 18, 32, .12);
      border-radius: 26px;
      padding: 1.25rem;
      box-shadow: 0 14px 34px rgba(100, 18, 32, .09);
    }}

    .time {{
      color: var(--wine);
      font-weight: 900;
      font-family: "Space Grotesk", sans-serif;
    }}

    .timeline-item h3 {{
      color: var(--burgundy);
      font-family: "Space Grotesk", sans-serif;
      margin-bottom: .3rem;
    }}

    .timeline-item p {{
      color: var(--muted);
      line-height: 1.7;
    }}

    .contact-box {{
      background: var(--burgundy);
      color: var(--cream);
      border-radius: 42px;
      padding: 3rem 2rem;
      text-align: center;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }}

    .contact-box::before {{
      content: "✦";
      position: absolute;
      font-size: 12rem;
      opacity: .08;
      left: 25px;
      top: -35px;
    }}

    .contact-box h2 {{
      font-family: "Space Grotesk", sans-serif;
      font-size: 2.6rem;
      margin-bottom: .8rem;
    }}

    .contact-box p {{
      opacity: .9;
      margin-bottom: 1.4rem;
    }}

    .socials {{
      display: flex;
      justify-content: center;
      gap: .8rem;
      margin-top: 1rem;
    }}

    .socials a {{
      width: 48px;
      height: 48px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      background: rgba(255, 243, 223, .15);
      color: var(--cream);
      text-decoration: none;
      font-size: 1.45rem;
    }}

    footer {{
      text-align: center;
      padding: 2rem;
      color: var(--muted);
      font-weight: 700;
    }}

    @media (max-width: 880px) {{
      .hero, .grid {{
        grid-template-columns: 1fr;
      }}

      .photo-card {{
        transform: none;
      }}

      .nav-links {{
        display: none;
      }}

      .mini-stats {{
        grid-template-columns: 1fr;
      }}

      .timeline-item {{
        grid-template-columns: 1fr;
      }}

      h1 {{
        letter-spacing: -1px;
      }}

      .photo-card img {{
        min-height: auto;
      }}
    }}
  </style>
</head>

<body>
  <header>
    <nav class="container">
      <a href="#" class="logo"><span>DK</span> Dhivya</a>
      <ul class="nav-links">
        <li><a href="#about">About</a></li>
        <li><a href="#skills">Skills</a></li>
        <li><a href="#work">Experience</a></li>
        <li><a href="#highlights">Highlights</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <section class="hero container">
      <div>
        <div class="eyebrow"><i class='bx bxs-star'></i> Aspiring Data Analyst • Web Developer</div>
        <h1>Data, design & a little <span class="cream-tag">funk.</span></h1>

        <p class="hero-text">
          I’m Dhivyadharshini Karunakaran, a Data Analytics graduate from the University of Galway with a B.Tech in Computer Science and Business Systems. I enjoy turning data into actionable insights through Python, R, Java, Machine Learning, Deep Learning, NLP, and web development.
        </p>

        <div class="cta-row">
          <a href="Profile.pdf" class="btn primary" download><i class='bx bx-download'></i> Download Resume</a>
          <a href="#highlights" class="btn secondary"><i class='bx bx-party'></i> See Highlights</a>
        </div>

        <div class="mini-stats">
          <div class="stat"><strong>MSc</strong><span>Data Analytics</span></div>
          <div class="stat"><strong>3+</strong><span>Research Highlights</span></div>
          <div class="stat"><strong>2024</strong><span>Galway Graduate</span></div>
        </div>
      </div>

      <div class="photo-card">
        <div class="sticker">AI techy me ✨</div>
        <img src="{ai_name}" alt="AI tech-inspired portrait of Dhivyadharshini Karunakaran">
        <div class="photo-caption">
          <h2>Data to Impact</h2>
          <p>Analyze • Insight • Solve</p>
        </div>
      </div>
    </section>

    <section id="about" class="container">
      <div class="section-head">
        <h2>About Me</h2>
        <p>Professional, but with personality.</p>
      </div>

      <div class="grid">
        <div class="card">
          <div class="icon"><i class='bx bx-bar-chart-alt-2'></i></div>
          <h3>Data Analytics</h3>
          <p>Strong interest in data cleaning, validation, reporting, and turning raw information into useful business insights.</p>
        </div>

        <div class="card">
          <div class="icon"><i class='bx bx-code-curly'></i></div>
          <h3>Web Development</h3>
          <p>Freelance web developer since November 2023, designing portfolio and complex websites with improved reliability and user experience.</p>
        </div>

        <div class="card">
          <div class="icon"><i class='bx bx-group'></i></div>
          <h3>Communication</h3>
          <p>Experience in client communication, documentation, teaching assistance, staff coordination, and fast-paced service environments.</p>
        </div>
      </div>
    </section>

    <section id="skills" class="container">
      <div class="section-head">
        <h2>Skill Splash</h2>
        <p>Funky badges, recruiter-friendly keywords.</p>
      </div>

      <div class="skills-wrap">
        <span class="skill">Python</span>
        <span class="skill">R Programming</span>
        <span class="skill">Java</span>
        <span class="skill">Machine Learning</span>
        <span class="skill">Deep Learning</span>
        <span class="skill">NLP</span>
        <span class="skill">Web Development</span>
        <span class="skill">Excel / Google Sheets</span>
        <span class="skill">GitHub</span>
        <span class="skill">Inventory Management</span>
        <span class="skill">Food Safety</span>
        <span class="skill">HACCP</span>
      </div>
    </section>

    <section id="work" class="container">
      <div class="section-head">
        <h2>Experience Timeline</h2>
        <p>A clean path through your technical, teaching, and leadership experience.</p>
      </div>

      <div class="timeline">
        <div class="timeline-item">
          <div class="time">Nov 2023 – Present</div>
          <div>
            <h3>Freelance Web Developer • Ireland</h3>
            <p>Designed and developed websites, improved user experience, managed client requirements, and maintained clear project documentation.</p>
          </div>
        </div>

        <div class="timeline-item">
          <div class="time">Sep 2024 – Jun 2026</div>
          <div>
            <h3>Deli Manager • Daybreak, Galway</h3>
            <p>Coordinated shifts, handled inventory and stock control, supported hiring, training, food safety, and service standards.</p>
          </div>
        </div>

        <div class="timeline-item">
          <div class="time">Oct 2024 – May 2025</div>
          <div>
            <h3>Teaching Assistant • University of Galway</h3>
            <p>Supported students in Fundamentals of Java and Web Development through labs, programming concepts, troubleshooting, and hands-on exercises.</p>
          </div>
        </div>

        <div class="timeline-item">
          <div class="time">Jan 2023 – Feb 2024</div>
          <div>
            <h3>Data Analysis Assistant • 8Queens, Chennai</h3>
            <p>Assisted with data collection, cleaning, validation, quality checks, reporting datasets, documentation, and version control.</p>
          </div>
        </div>

        <div class="timeline-item">
          <div class="time">Feb 2022 – Dec 2022</div>
          <div>
            <h3>Project Intern • Paxel Indonesia, Chennai</h3>
            <p>Developed and tested Java modules, documented implementations, and collaborated with cross-functional teams.</p>
          </div>
        </div>
      </div>
    </section>

    <section id="highlights" class="container">
      <div class="section-head">
        <h2>Highlights Wall</h2>
        <p>Your best bits, displayed like funky achievement cards.</p>
      </div>

      <div class="grid">
        <div class="card">
          <div class="icon"><i class='bx bx-trophy'></i></div>
          <h3>Best Paper Award</h3>
          <p>Recognised for the publication “Roll Call Tracking System for Education Sectors Using Face Recognition System.”</p>
        </div>

        <div class="card">
          <div class="icon"><i class='bx bx-rocket'></i></div>
          <h3>iDEX Shortlist</h3>
          <p>Shortlisted for High Powered Selection Committee Presentation of iDEX DISC #6 Defence Innovation Organization among 200+ teams.</p>
        </div>

        <div class="card">
          <div class="icon"><i class='bx bx-certification'></i></div>
          <h3>Certifications</h3>
          <p>Java, Python, JavaScript, Introduction to CSS, and Introduction to Programming Using Python.</p>
        </div>
      </div>
    </section>

    <section class="container">
      <div class="section-head">
        <h2>Education</h2>
        <p>Your academic story in one neat row.</p>
      </div>

      <div class="grid">
        <div class="card">
          <div class="icon"><i class='bx bxs-graduation'></i></div>
          <h3>University of Galway</h3>
          <p>MSc Computer Science, Data Analytics<br>September 2024 – May 2025</p>
        </div>

        <div class="card">
          <div class="icon"><i class='bx bx-laptop'></i></div>
          <h3>Sri Sairam Engineering College</h3>
          <p>B.Tech Computer Science and Business Systems<br>January 2020 – May 2024</p>
        </div>

        <div class="card">
          <div class="icon"><i class='bx bx-book-heart'></i></div>
          <h3>St. Dominic’s Anglo Indian HSS</h3>
          <p>Schooling<br>May 2009 – March 2020</p>
        </div>
      </div>
    </section>

    <section id="contact" class="container">
      <div class="contact-box">
        <h2>Let’s make data cute and useful.</h2>
        <p>Dublin, Ireland • +353 892301616 • dhivyak0210@gmail.com</p>
        <a class="btn secondary" href="mailto:dhivyak0210@gmail.com"><i class='bx bx-envelope'></i> Email Me</a>
        <div class="socials">
          <a href="https://www.linkedin.com/in/dd02/" aria-label="LinkedIn"><i class='bx bxl-linkedin'></i></a>
          <a href="https://dhivyak0210.github.io/Portfolio/" aria-label="Portfolio"><i class='bx bx-globe'></i></a>
        </div>
      </div>
    </section>
  </main>

  <footer>
    © 2026 Dhivyadharshini Karunakaran • Burgundy & cream portfolio
  </footer>
</body>
</html>
"""

(out / "index.html").write_text(html, encoding="utf-8")

zip_path = Path("/mnt/data/burgundy_portfolio_with_ai_photo.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for file in out.iterdir():
        z.write(file, file.name)

print(f"Created: {out / 'index.html'}")
print(f"Created: {zip_path}")
