![image](https://user-images.githubusercontent.com/61703252/223690036-07cbe8a5-5233-44d7-b0b5-a418fe41564e.png)
<h1> Tile Master </h1>
<p>
  Tile Master is an web application written in React.js, that interacts with the Python backend in real-time to operate a robot, which purpose was to
  push the colored tiles on a factory line. The app is responsive, so it works both for phone, tablet and computer screens.
</p>
<p>
  Previously, the robot was hosted on a raspberry PI, which operated the electrical components according to the requests sent by the users.
  Unfortunately, there are no electrical components anymore. There is however a real-time web application to demonstrate the capabilities and
  interactivity of the robot.
</p>
<h2>Capabilities</h2>
<p>
  Through the Tile Master web app, the user could:
  <ul>
    <li>Arbitrairly program the robot behaviour with pre-designed instructions</li>
    <li>Use the pre-made useful utilities, like sorting or displaying Morse Code</li>
    <li>Switch the robot to the manual mode, which stops the instruction execution and lets the user push the arm manually</li>
    <li>See all of the actions performed by robot's components</li>
    <li>See the counter of the tiles detected by the robot's scanner</li>
   </ul>
   It is important to note, that this is a <b>real time</b> application, which means that all of the events are immediately updated on all of 
   the devices that have the app opened. This has been achieved by using HTTP Polling - we could have used websockets but we are only students!
</p>

<h2>How to run it</h2>
<p>
  To run the project, you need to run a python program that works as a server.
  This is a python program, so you need a python interpreter (3.8 or higher).
</p>
<p>
  Firstly however, you need to install all of the dependencies. Go to the raspberry directory:
  <code>cd raspberry</code>
  Then install the dependencies and run the script:
  <h4>For Windows:</h4>
  <code>    pip install -r requirements.txt
    python run_testing.py</code>
  <h4>For Linux/Mac:</h4>
  <code>    python3 -m pip install -r requirements.txt
    python3 run_testing.py</code></br>
  Then, every device on the same network can connect to it by
  typing in its <b>ip:5000</b> (for example 192.168.0.20:5000) into the browser. On the same device, you can run localhost:5000 to connect to it.
</p>
