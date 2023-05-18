# Spotify-Downloader-Python
this repo contains a program that allows me to automate any added song into a specific Spotify-playlist to be downloaded . So i can download the song whenever i want just by adding it to the chosen Spotify-library
## all you need to change to make it yours
<ul>
  <li>Delete <code>prv.pckl</code> file, the problem here that each playlist will need an object, and each object will need a pickle file. So it's a bad strategy but it works</li>
  <li>change the two variables <code>SAVE_FILE</code>, <code>all_my_Playlists</code></li>
  <li>you need to write your own Variables<code>my_export_variables</code> for the Credentials, my way was writing the variables in different text file just for privacy.<br> you can make your own file and put it where ever you want but make sure to read it in the code <br><img src='https://github.com/Abdulrahman-Yasser/Spotify-Downloader-Python/assets/63866803/4203dbf5-10c0-438b-86fb-b2af5419e244'></li>  
</ul>

### To automate it in your PC
<ul>
  <li>Open Task scheduler</li>
  <li>Choose Create basic task<br>
  <img src='https://github.com/Abdulrahman-Yasser/Youtube-Downloader-Python/assets/63866803/7bb2f44c-2b29-4c43-b1ff-cf1711d8299b'>
  </li>
  <li>Put the name you want and description then press next<br>
    <img src='https://github.com/Abdulrahman-Yasser/Youtube-Downloader-Python/assets/63866803/98320e39-926f-4473-8b31-18213fd9934b'>
  </li>
  <li>Choose the schedule that suits you<br>
    <img src='https://github.com/Abdulrahman-Yasser/Youtube-Downloader-Python/assets/63866803/cc5cd81f-716b-4d1a-a957-8c20e7e32c0a'>
  </li>
  <li>Choose start a program<br>
    <img src='https://github.com/Abdulrahman-Yasser/Youtube-Downloader-Python/assets/63866803/ba4e8050-9412-4d2f-9483-4ee85a1fbc1b'>
  </li>
  <li>first you need to input your python location, you can get it using the <code>where python</code><br>
  </li>
  <li>then you need to put the python script name in the Add argument cell.
  </li>
  <li>put the python script location in the start in cell<br>
    <img src='https://github.com/Abdulrahman-Yasser/Youtube-Downloader-Python/assets/63866803/cb9ff30a-89f0-4bc6-99d1-1dfab998871d'>
  </li>
</ul>
