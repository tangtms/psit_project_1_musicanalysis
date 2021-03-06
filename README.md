# TopChart Music Analysis
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;โปรเจคนี้มีวัตถุประสงค์เพื่อ วิเคราะห์พฤติกรรมการฟังเพลงของคนไทยที่ใช้บริการ Spotify
โดยสถิติที่เรานำมาวิเคราะห์ได้มาจากเว็บของ Spotifyโดยตรง ซึ่งที่ข้อมูลเรานำมาใช้นั้น
เริ่มตั้งแต่เดือนกันยายน 2017 – สิงหาคม 2018 โดยจำแนกตามประเภท เพลงไทย/ต่างประเทศ
ศิลปินยอดนิยมประจำเดือน/ประจำปี วิเคราะห์ศิลปิน และวิเคราะห์ปัจจัยที่ทำให้ยอดอัตราการ
สตรีมมิ่งเพลงถึงสูงขึ้นในช่วงๆหนึ่ง

## Topics
* **Thai music/ International music**
อัตราส่วนเพลงไทย/เพลงนานาชาติ
* **Stream count monthly**
กราฟยอดสตรีมมิ่งรายเดือน
* **Artist of the month**
กราฟอัตราการส่วนการฟังเพลงของศิลปินในแต่ละเดือน
* **Top 10 Artists of the year**
10 อันดับศิลปินแห่งปี
* **Top 5 Artists Analysis**
ยอดสตรีมมิ่งรายเดือนของศิลปิน 5 อันดับแรก
* **Thai music and International music Analysis**
กราฟอัตราการส่วนการฟังเพลงของศิลปินในแต่ละเดือน

## Results
* [Website](http://www.it.kmitl.ac.th/~it61070103/WEB/index.html)
* [Youtube](https://youtu.be/8BghPck5udw)

## Data Sources
#### [SpotifyCharts - Spotify](https://spotifycharts.com/regional/th/weekly/latest)
##### **ช่วงเวลาของข้อมูล -** September 2017 - August 2018* (1 ปี)

## Directory Structure
* `data` - ไฟล์ csv ทั้งหมด
* `convert` - ไฟล์ python รวม csv เข้าด้วยกันและแปลงเป็น dict
* `visualize`
  * `dict_file` - ไฟล์ dict และไฟล์ python
  * `graph` - ไฟล์กราฟ svg 6 กราฟ
* `web` - เว็บไซต์ของโปรเจค

## Built-With
* Python `3.7.0`
    * pygal `2.0.0`

## Authors
สามเกลอสยึมกึ๋ย
* นายธนวัฒน์ เขมวัชรเลิศ - 61070074 - [zimbo333](https://github.com/zimbo333)
* นายธรรมสรณ์ ตันติยาภินันท์ - 61070084 - [tangtms](https://github.com/tangtms)
* นายนันทวัฒน์ สุธางค์กรกุล - 61070103 - [nun0289](https://github.com/nun0289)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)