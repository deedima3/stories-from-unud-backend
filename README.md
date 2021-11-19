# Application Program Website Blog Unud
<p align="center"><img align="center" src="https://upload.wikimedia.org/wikipedia/id/2/2d/Logo-unud-baru.png"></p>
Kumpulan artikel seputar Universitas Udayana.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.

```bash
pip install -r requirements.txt
```

## Start Server

```bash
python manage.py runserver
```

## API Reference
<h3 align="center">1. Get All Article</h3>
<h4 align="center">URL : https://unud-blog.herokuapp.com/api/blog-post </h4>
#### 

```http
   [POST] /api/blog-post/
```


| JSON Body | Type     | Description                |Default Value|
| :-------- | :------- | :------------------------- |:------|
| `format`| `string` | **Optional**.  |api|

#### Json Response

```javascript
[
  {
    "HashNumber": 59,
    "title": "teknik udayana",
    "article": "Fakultas Teknik Universitas Udayana secara resmi berdiri pada tanggal 1 Oktober 1965 dengan Surat Keputusan Menteri PTIP No. 248/Sek/P.U/1965, tanggal 20 Oktober 1965, yang terdiri dari dua jurusan yaitu Jurusan Arsitektur dan Jurusan Seni Rupa. Sebagai latar belakang pendirian Fakultas Teknik Universitas Udayana, adalah dalam rangka pelestarian, pengembangan kebudayaan Daerah Bali pada khususnya dan kebudayaan nasional pada umumnya, terutama di dalam menghadapi pembangunan dan perkembangan kepariwisataan.",
    "dateTimeCreated": "2021-11-19T10:40:40.842714Z",
    "author": "Jeremi",
    "visitor": 0
  },
  {
    "HashNumber": 205,
    "title": "universitas udayana",
    "article": "Sejarah - Cikal bakal Universitas Udayana adalah Fakultas Sastra cabang Universitas Airlangga yang diresmikan oleh P. J. M. Presiden Republik Indonesia Ir. Soekarno, dibuka oleh J. M. Menteri P.P dan K. Prof. DR. Priyono pada tanggal 29 September 1958 sebagaimana tertulis pada Prasasti di Fakultas Sastra, Jalan Nias, Denpasar. Universitas Udayana secara sah berdiri pada tanggal 17 Agustus 1962 dan merupakan perguruan tinggi negeri tertua di daerah Provinsi Bali. Sebelumnya, sejak tanggal 29 September 1958 di Bali sudah berdiri sebuah fakultas yang bernama fakultas Sastra Udayana sebagai cabang dari Universitas Airlangga.\\r\\n\\r\\nFakultas Sastra Udayana inilah yang merupakan embrio daripada berdirinya Universitas Udayana. Berdasarkan Surat Keputusan Menteri PTIP No.104/1962, tanggal 9 Agustus 1962, Universitas Udayana secara sah berdiri sejak tanggal 17 Agustus 1962. Akan tetapi, karena hari lahir Universitas Udayana jatuh bersamaan dengan hari Proklamasi Kemerdekaan Republik Indonesia, maka perayaan hari ulang tahun Universitas Udayana dialihkan menjadi tanggal 29 September dengan mengambil tanggal peresmian fakultas sastra yang telah berdiri sejak tahun 1958.[8].",
    "dateTimeCreated": "2021-11-19T10:43:27.123226Z",
    "author": "Admin",
    "visitor": 0
  },
  {
    "HashNumber": 110,
    "title": "fmipa udayana",
    "article": "Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA) Universitas Udayana terbentuk melalui beberapa tahap. Pada 1984 dibentuk Jurusan Kimia dan Fisika. Pada tahun 1985 dibentuk Jurusan Biologi, dilanjukan dengan jurusan matematka pada tahun 2000 dan terakhir jurusan Farmasi diijinkan 2005.",
    "dateTimeCreated": "2021-11-19T10:43:55.754299Z",
    "author": "Admin",
    "visitor": 0
  }
]
```

#### 
<h3 align="center">2. Get One Article</h3>
<h4 align="center">URL : https://unud-blog.herokuapp.com/api/blog-post/one-item </h4>

```http
  [POST] /api/blog-post/one-item/
```

| JSON Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `HashNumber`      | `string` | **Required** |

#### Example http

```http
  [GET] /api/blog-post/one-item/?token=***?HashNumber=57
```
#### Example
![static/img_1.png](static/img_2.png)

#### 
<h3 align="center">3. Search Article</h3>
<h4 align="center">URL : https://unud-blog.herokuapp.com/api/search </h4>

```http
  [POST] /api/search/
```

| JSON Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `keyword`      | `string` | **Required** |

#### Example
![static/img_1.png](static/img_1.png)

#### 
<h3 align="center">4. Create New Article</h3>
<h4 align="center">URL : https://unud-blog.herokuapp.com/api/create/article </h4>

```http
  [POST] /api/create/article/
```

| Multipart | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required** - Judul Artikel|
| `article`    | `string` | **Required** - Isi Artikel |
| `author`      | `string` | **Required** - Penulis Artikel|

#### Example
![img.png](static/img.png)

#### 
<h3 align="center">5. Admin Validator</h3>
<h4 align="center">URL : https://unud-blog.herokuapp.com/api/adminValidator </h4>

```http
  [GET/POST] /api/adminValidator/
```

| Multipart | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required** |
| `...`      | `...` | **...** |

#### Json Response
```javascript
    NOT IMPLEMENTED, ON PROGRESS
```
  