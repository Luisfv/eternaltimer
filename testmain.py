#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
form = """
<DOCTYPE html>
<html>

    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="description" content="">
      <meta name="author" content="">
      <link rel="shortcut icon" href="../../docs-assets/ico/favicon.png">

      <title>Eternal Timer</title>

      <!-- Bootstrap core CSS -->
      <link href="../../dist/css/bootstrap.css" rel="stylesheet">

      <!-- Custom styles for this template -->
      <link href="starter-template.css" rel="stylesheet">

      <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
      <![endif]-->
    </head>
    
    <body>

      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Eternal Timer</a>
          </div>
          <div class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>

      <div class="container">

        <div class="starter-template">
          <h1>Eternal Timer</h1>
          <p class="lead">

    </div><!-- /.container -->

        <!--This is the FB comments Javascript SDK thingy
        <div id="fb-root"></div>
        <script>(function(d, s, id) {
          var js, fjs = d.getElementsByTagName(s)[0];
          f (d.getElementById(id)) return;
          js = d.createElement(s); js.id = id;
          js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
          fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));</script>
        -->

        <h1 style = "font-size: 50px; font-family: Impact; color: blue; text-align: center; background-color: ">
          <center><table>
            <tr>
              <td style = "color: blue; background-color: black; text-align: center; font-size: 50px"><em><b>Eternal Timer</b></em></td>
            </tr>
          </table></center>
        </h1>
        
        <p style = "text-align: center">
          Ever been distracted on Facebook and wasted precious studying time?<br><br>
          Well now, after extensive psychological research and countless hours of hard manual labor, the team at<br><br>
          <b><em>Eternal Timer&trade; </b></em><br><br>
          has found a perfect, flawless solution!<br><br>
          <br>
          How can this be possible??<br><br>
          <em><b>This application will revolutionize studying sessions everywhere!<br><br> 
          With the most sophisticated of development techniques, we have given birth to Eternal Timer.<br><br>
          With this application, you can keep track of the hours spent studying like magic!<br><br>
          With the simple click of a button, Eternal Timer&trade; will begin timing you. <br><br>
          When you are finished studying, you will be asked to record your work with pictures. <br><br>
          These pictures will be posted on your Facebook wall with a congratulatory message. <br><br>
          However, if you end up goofing off and not studying, a degrading message will be posted on your wall! <br><br>
          This foolproof design will force you to study or face public shame!</b></em>
        </p>
        
        <!-- Taking Google off for a little bit
        
        <h1>
          <img src = "https://www.google.com/images/srpr/logo3w.png" alt = "Google"/>
        </h1>
        
        <form action = "http://www.google.com/search">
          <input name = "q">
          <input type = "Submit">
        </form>
        
        -->

        <!-- Youtube Video -->
        <h2 style = "color: blue; text-align: center; font-size: 30px">
          <b> Here is another amazing production by the same team!</b>
        </h2>

        <p style = "text-align: center">
          <iframe width="853" height="480" src="http://www.youtube.com/embed/vy7bSy-hxL0" frameborder="0" allowfullscreen></iframe>
        </p>

        <!-- Funny Picture -->
        <h1 style = "color: blue; text-align: center">
          <b> <a href = "http://oi46.tinypic.com/qys608.jpg"> Funny picture of the day!</a> </b>
        </h1>
        
        <p style = "text-align: center">
          <img src = "http://oi46.tinypic.com/qys608.jpg" alt = "Funny Picture"/>
        </p>  

        
         <center><iframe src="//www.facebook.com/plugins/like.php?href=http%3A%2F%2Fzyloline.appspot.com%2F&amp;send=false&amp;layout=standard&amp;width=450&amp;show_faces=true&amp;font=verdana&amp;colorscheme=light&amp;action=like&amp;height=60" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:450px; height:60px;"
          allowTransparency="true"></iframe></center>
        
        <div class="fb-comments" data-href="http://zyloline.appspot.com/" data-width="470" data-num-posts="10" data-colorscheme="dark"></div>

      <!-- Bootstrap core JavaScript
      ================================================== -->
      <!-- Placed at the end of the document so the pages load faster -->
      <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
      <script src="../../dist/js/bootstrap.min.js"></script>
    </body>
</html>

"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.out.write(q)
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/testform', TestHandler)], debug=True)
