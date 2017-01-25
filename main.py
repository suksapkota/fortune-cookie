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
import random

class MainHandler(webapp2.RequestHandler):
    def getRandomFortune(self):
        fortune=["A smile is your passport into the hearts of others.","A friend asks only for your time not your money.",
                "A good way to keep healthy is to eat more Chinese food.","Enjoy the good luck a companion brings you.",
                "Your high-minded principles spell success."]
        display=random.choice(fortune)
        return display

    def get(self):
        title ="<h1> Fortune Cookie </h1>"

        luck= "<strong>"+self.getRandomFortune() +"</strong>"
        fortune_sentence="Your Fortune: "+luck
        fortune_para="<p>" + fortune_sentence+"</p>"

        number="<strong>"+ str(random.randint(1,100))+ "</strong>"
        num_sentence="Your Luky Number: "  +number
        num_para="<p>" + num_sentence+"</p>"

        cookie_button=  "<a href= '.'> <button>Another cookie please</button> </a>"

        content= title+fortune_para+num_para + cookie_button
        self.response.write(content)






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
