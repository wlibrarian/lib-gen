base = [
"""
<!DOCTYPE html>
<html lang="en-GB">

<head>
    <title>Librarian Online - ""","""</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/main.css">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/article.css">
	<link href="https://fonts.googleapis.com/css?family=Lato:400,400i,700,700i" rel="stylesheet">
</head>

<body>
    <header>
        <div id='top'>
        <a href="https://librarian.cf" style="display: block;">
        <div id='logo'>
            <object style="pointer-events: none;" type="image/svg+xml" data="https://librarian.cf/media/logo.svg">Your browser does not support SVG</object>
        </div>
        </a>
        <nav>
            <a href="https://librarian.cf/" class="nav">Home</a> &vellip;
            <a href="https://librarian.cf/d.html" class="nav">Dialectic</a> &vellip;
            <a href="https://librarian.cf/r.html" class="nav">Review</a> &vellip;
            <a href="https://librarian.cf/s.html" class="nav">Sciences and mathematics</a> &vellip;
            <a href="https://librarian.cf/i.html" class="nav">Issues</a> &vellip;
            <a href="https://librarian.cf/l.html" class="nav">Letters</a> &vellip;
            <a href="https://librarian.cf/e.html" class="nav">Editorial</a>
        </nav>
        </div>
    </header>

    <main>
        <aside class="fill"></aside>
        <aside class="meta provenance">""","""
        </aside>
        <article>""","""
        </article>
        <aside class="meta topics">""","""
        </aside>
        <aside class="fill"></aside>
    </main>
</body>

</html>
"""
]
maths = [
"""
<!DOCTYPE html>
<html lang="en-GB">

<head>
    <title>Librarian Online - ""","""</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/main.css">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/article.css">
	<link href="https://fonts.googleapis.com/css?family=Lato:400,400i,700,700i" rel="stylesheet">
    <script type="text/javascript" async
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
    </script>
</head>

<body>
    <header>
        <div id='top'>
        <a href="https://librarian.cf" style="display: block;">
        <div id='logo'>
            <object style="pointer-events: none;" type="image/svg+xml" data="https://librarian.cf/media/logo.svg">Your browser does not support SVG</object>
        </div>
        </a>
        <nav>
            <a href="https://librarian.cf/" class="nav">Home</a> &vellip;
            <a href="https://librarian.cf/d.html" class="nav">Dialectic</a> &vellip;
            <a href="https://librarian.cf/r.html" class="nav">Review</a> &vellip;
            <a href="https://librarian.cf/s.html" class="nav">Sciences and mathematics</a> &vellip;
            <a href="https://librarian.cf/i.html" class="nav">Issues</a> &vellip;
            <a href="https://librarian.cf/l.html" class="nav">Letters</a> &vellip;
            <a href="https://librarian.cf/e.html" class="nav">Editorial</a>
        </nav>
        </div>
    </header>

    <main>
        <aside class="fill"></aside>
        <aside class="meta provenance">""","""
        </aside>
        <article>""","""
        </article>
        <aside class="meta topics">""","""
        </aside>
        <aside class="fill"></aside>
    </main>
</body>

</html>
"""
]

front = ["""<!DOCTYPE html>
<html lang="en-GB">

<head>
    <title>The Librarian Online</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/main.css">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/front.css">
	<link href="https://fonts.googleapis.com/css?family=Lato:400,400i,700,700i" rel="stylesheet">
</head>

<body>
    <header>
        <div id='top'>
        <a href="https://librarian.cf" style="display: block;">
        <div id='logo'>
            <object style="pointer-events: none;" type="image/svg+xml" data="https://librarian.cf/media/logo.svg">Your browser does not support SVG</object>
        </div>
        </a>
        <nav>
            <a href="https://librarian.cf/" class="nav">Home</a> &vellip;
            <a href="https://librarian.cf/d.html" class="nav">Dialectic</a> &vellip;
            <a href="https://librarian.cf/r.html" class="nav">Review</a> &vellip;
            <a href="https://librarian.cf/s.html" class="nav">Sciences and mathematics</a> &vellip;
            <a href="https://librarian.cf/i.html" class="nav">Issues</a> &vellip;
            <a href="https://librarian.cf/l.html" class="nav">Letters</a> &vellip;
            <a href="https://librarian.cf/e.html" class="nav">Editorial</a>
        </nav>
        </div>
    </header>
    <main>
      <section>
        <aside class='fill'></aside>
        <section class="container">
          <h1 class='heading'>Home</h1>
          <a href="d.html" class="nav"><h1 class="heading">Dialectic</h1></a>
          <section>""","""
          </section>
        </section>
        <section class="container">
          <h1 class='heading'></h1>
          <a href="i.html" class="nav"><h1 class="heading">Issues</h1></a>
          <section>""","""
          </section>
        </section>
        <aside class='fill'></aside>
      </section>

      <section>
        <aside class='fill'></aside>
        <section class="container">
          <a href="l.html" class="nav"><h1 class="heading">Letters</h1></a>
          <section>""","""
          </section>
        </section>
        <section class="container">
          <a href="r.html" class="nav"><h1 class="heading">Review</h1></a>
          <section>""","""
          </section>
        </section>
        <aside class='fill'></aside>
      </section>

      <section>
        <aside class='fill'></aside>
        <section class="container">
          <a href="s.html" class="nav"><h1 class="heading">Sciences and Mathematics</h1></a>
          <section>""","""
          </section>
        </section>
        <section class="container">
          <a href="e.html" class="nav"><h1 class="heading">Editorial</h1></a>
          <section>""","""
          </section>
        </section>
        <aside class='fill'></aside>
      </section>
    </main>
</body>

</html>"""]

topic = ["""
<!DOCTYPE html>
<html lang="en-GB">

<head>
    <title>The Librarian Online</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/main.css">
    <link rel="stylesheet" type="text/css" href="https://librarian.cf/stylesheets/front.css">
	<link href="https://fonts.googleapis.com/css?family=Lato:400,400i,700,700i" rel="stylesheet">
</head>

<body>
    <header>
        <div id='top'>
        <a href="https://librarian.cf" style="display: block;">
        <div id='logo'>
            <object style="pointer-events: none;" type="image/svg+xml" data="https://librarian.cf/media/logo.svg">Your browser does not support SVG</object>
        </div>
        </a>
        <nav>
            <a href="https://librarian.cf/" class="nav">Home</a> &vellip;
            <a href="https://librarian.cf/d.html" class="nav">Dialectic</a> &vellip;
            <a href="https://librarian.cf/r.html" class="nav">Review</a> &vellip;
            <a href="https://librarian.cf/s.html" class="nav">Sciences and mathematics</a> &vellip;
            <a href="https://librarian.cf/i.html" class="nav">Issues</a> &vellip;
            <a href="https://librarian.cf/l.html" class="nav">Letters</a> &vellip;
            <a href="https://librarian.cf/e.html" class="nav">Editorial</a>
        </nav>
        </div>
    </header>
    <main>
        <section>
            <aside class='fill'></aside>
            <section class='container'>
                <h1 class='heading'>""","""</h1>""","""
            </section>
            <aside class='fill'></aside>
        </section>
    </main>
</body>

</html>
"""]
