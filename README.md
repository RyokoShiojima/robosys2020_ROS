# robosys2020_ROS

### 実装内容
 - publisherが入力したメッセージとメッセージが送信された時刻を送信する。
 - subscliberはpublisherが送信したメッセージを受信する。(英語に翻訳するバージョンもある)

### 実装環境
|             |              |     | 
| ----------- | ------------ | --- | 
| OS          | ubuntu 20.04 |     | 
| ROS         | noetic       |     | 
| Python      | 3.8.5        |     | 
| googletrans | 4.0.0-rc1    |     | 

### ROSの環境構築方法
 - 下記のリンクのスクリプトを使用してROSの環境構築を行います。
   [ros_setuo_scripts_Ubuntu20.04](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server)

### パッケージのインストール方法
```sh
$ cd ~/catkin_ws/src
$ git clone https://github.com/RyokoShiojima/robosys2020_ROS.git
```

### googletransのインストール方法
```sh
$ pip3 install googletrans==4.0.0-rc1
```

### 実行方法
 - パッケージをビルド
 ```sh
 $ cd ~/catkin_ws
 $ catkin_make
 $ source ~/.bashrc
 ```
 
 - プログラムの実装
  - 端末1 
  ```sh
  $ cd ~/catkin_ws/src/robosys2020_ROS/scripts
  $ roscore
  ```

  - 端末2
  ```sh
  $ cd ~/catkin_ws/src/robosys2020_ROS/scripts
  $ rousrun robosys2020_ROS speaker.py
  ```

  - 端末3

   - 英語翻訳なし
   ```sh
   $ cd ~/catkin_ws/src/robosys2020_ROS/scripts
   $ rousrun robosys2020_ROS listener.py
   ```

   - 英語翻訳あり
   ```sh
   $ cd ~/catkin_ws/src/robosys2020_ROS/scripts
   $ rousrun robosys2020_ROS listener_english.py
   ```

   - 終了するにはそれぞれの端末でctrl+c

### 実演動画

 - 画像をクリックすると動画のリンクに飛びます

  - 翻訳なしバージョン
  [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/DbEM8GMXG3I/0.jpg)](https://youtu.be/DbEM8GMXG3I) 

  - 翻訳ありバージョン[こちら↓](https://youtu.be/7IUDDHJ30jg)
  [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/7IUDDHJ30jg/0.jpg)](https://youtu.be/7IUDDHJ30jg)

## LICENCE
 - googletrans:[MIT Licence](https://pypi.org/project/googletrans/4.0.0rc1/)
 - ROS:[BSD 3-Clause License](https://github.com/RyokoShiojima/robosys2020_ROS/blob/main/LICENSE)
