<h1>Log Monitoring for Security Incidents</h1>

<p>A Python-based tool for monitoring system logs to detect potential security incidents like brute-force login attempts and failed SSH logins.</p>

<h2>Features:</h2>
<ul>
  <li>Parse system logs (<code>/var/log/auth.log</code>)</li>
  <li>Detect brute-force login attempts</li>
  <li>Send email alerts when suspicious activity is detected</li>
  <li>Configure multiple email recipients for alerts</li>
</ul>

<h2>Requirements:</h2>
<ul>
  <li>Python 3.x</li>
  <li><code>smtplib</code></li>
  <li><code>re</code></li>
  <li><code>os</code></li>
  <li><code>dotenv</code> (for loading environment variables)</li>
</ul>

<h2>Setup:</h2>
<ol>
  <li>Clone this repository.</li>
  <li>Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>Create a <code>.env</code> file with your email credentials:
    <pre><code>EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password</code></pre>
  </li>
  <li>Run the script:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

<h2>Customization:</h2>
<ul>
  <li>Input a comma-separated list of email addresses to receive alerts.</li>
  <li>Modify the log file path if necessary.</li>
</ul>
