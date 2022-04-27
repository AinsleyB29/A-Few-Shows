from peewee import *
from datetime import date
from flask import Flask, jsonify, request

from playhouse.shortcuts import model_to_dict, dict_to_model


db = PostgresqlDatabase('shows', user='ainsleybrundage', password='', host='localhost', port=5432)



class BaseModel(Model):
    class Meta:
        database = db

class Show(BaseModel):
    name = CharField()
    releaseDate = DateField()
    description = CharField(max_length=3000)

db.connect()
db.drop_tables([Show])
db.create_tables([Show])


Show(name='Severance', releaseDate=date(2022, 2, 18), description='Mark leads a team of office workers whose memories have been surgically divided between their work and personal lives; when a mysterious colleague appears outside of work, it begins a journey to discover the truth about their jobs.').save()

Show(name='Homecoming', releaseDate=date(2018, 11, 2), description='A caseworker at a facility that helps soldiers transition back to civilian life leaves to start a new life, living with her mother and working as a small-town waitress.').save()

Show(name='Atlanta', releaseDate=date(2016, 9, 6), description='Atlanta is one of the top cities for young rappers looking to make a name for themselves in the business. Among those up-and-comers is Alfred Miles, a hot new artist who is trying to understand the line between real life and street life. He is managed by his cousin, Earn, who gets caught up in the local rap scene and his cousin''s career after returning home to the ATL. Earn does whatever he can to try to get Alfred''s career to the next level. Darius, the rapper''s right-hand man and visionary, is also in Alfred''s entourage. When Earn isn''t busy managing his cousin''s career, he spends much of his time with best friend Vanessa, who is also the mother of his daughter.').save()

Show(name='Abbott Elementary', releaseDate=date(2021, 12, 7), description='A group of dedicated, passionate teachers -- and a slightly tone-deaf principal -- find themselves thrown together in a Philadelphia public school where, despite the odds stacked against them, they are determined to help their students succeed in life. Though these incredible public servants may be outnumbered and underfunded, they love what they do -- even if they don''t love the school district''s less-than-stellar attitude toward educating children.').save()

Show(name='Ozark', releaseDate=date(2017, 7, 21), description='Created by Bill Dubuque ("The Accountant," "The Judge"), this drama series stars Jason Bateman as Marty Byrde, a financial planner who relocates his family from Chicago to a summer resort community in the Ozarks. With wife Wendy and their two kids in tow, Marty is on the move after a money-laundering scheme goes wrong, forcing him to pay off a substantial debt to a Mexican drug lord in order to keep his family safe. While the Byrdes'' fate hangs in the balance, the dire circumstances force the fractured family to reconnect.').save()

Show(name='Dark', releaseDate=date(2017, 12, 1), description='When two children go missing in a small German town, its sinful past is exposed along with the double lives and fractured relationships that exist among four families as they search for the kids. The mystery-drama series introduces an intricate puzzle filled with twists that includes a web of curious characters, all of whom have a connection to the town''s troubled history -- whether they know it or not. The story includes supernatural elements that tie back to the same town in 1986. "Dark" represents the first German original series produced for Netflix.').save()

Show(name='Westworld', releaseDate=date(2016, 10, 2), description='Westworld isn''t your typical amusement park. Intended for rich vacationers, the futuristic park -- which is looked after by robotic "hosts" -- allows its visitors to live out their fantasies through artificial consciousness. No matter how illicit the fantasy may be, there are no consequences for the park''s guests, allowing for any wish to be indulged. "Westworld" is based on the 1973 Michael Crichton movie of the same name and features an all-star cast.').save()

Show(name='Archive 81', releaseDate=date(2022, 1, 14), description='An archivist takes a job restoring damaged videotapes, but finds themselves getting pulled into a mystery involving the missing director and a mysterious cult that they were documenting.').save()

Show(name='Mindhunter', releaseDate=date(2017, 10, 13), description='Catching a criminal often requires the authorities to get inside the villain''s mind to figure out how he thinks. That''s the job of FBI agents Holden Ford and Bill Tench. They attempt to understand and catch serial killers by studying their damaged psyches. Along the way, the agents pioneer the development of modern serial-killer profiling. The crime drama has a strong pedigree behind the camera, with Oscar-nominated director David Fincher and Oscar-winning actress Charlize Theron among the show''s executive producers.').save()

Show(name='The Sinner', releaseDate=date(2017, 8, 2), description='Detective Harry Ambrose investigates a chilling new homicide each season. He employs some unusual tactics and a deep capacity for empathy to solve his cases. His boundless dedication is driven by his dark past, leading him into powerful and often dangerously intimate bonds with his suspects. "The Sinner" is a blend of a thrilling murder investigation and raw character drama, creating an electrifying ride with standout performances. The series was originally adapted from the novel of the same name by Petra Hammesfahr; however, the book''s darker outlook was toned down, and the location was shifted from Germany to Upstate New York.').save()

Show(name='The OA', releaseDate=date(2016, 12, 16), description='In addition to her role as creator and executive producer of this mind-bending series, Brit Marling also plays the role of Prairie Johnson, a young woman who returns home after a 7-year disappearance. Her sudden return is not the only miraculous occurrence: everyone is shocked to learn that Prairie is no longer blind. While the FBI and her parents are anxious to discuss Prairie''s disappearance, she won''t talk about what happened during the time that she was missing. Zal Batmanglij, the co-creator and an executive producer of the series, is the director of every episode.').save()

Show(name='The Night Of', releaseDate=date(2016, 6, 24), description='Based on the BBC series "Criminal Justice," HBO''s eight-part production "The Night Of" stars John Turturro ("O Brother, Where Art Thou?") and Riz Ahmed ("Nightcrawler") in a story about a complex New York City murder case with cultural and political overtones. A night that begins innocently for Pakistani-American college student Nasir "Naz" Khan turns horrific after he meets a mysterious young woman. In custody and awaiting his formal arraignment, Naz realizes that his survival -- or perhaps his demise -- rests not with his attorney, John Stone, but with a particular inmate at Rikers Island.').save()

Show(name='Money Heist', releaseDate=date(2017, 5, 2), description='A criminal mastermind who goes by "The Professor" has a plan to pull off the biggest heist in recorded history -- to print billions of euros in the Royal Mint of Spain. To help him carry out the ambitious plan, he recruits eight people with certain abilities and who have nothing to lose. The group of thieves take hostages to aid in their negotiations with the authorities, who strategize to come up with a way to capture The Professor. As more time elapses, the robbers prepare for a showdown with the police.').save()

Show(name='Maid', releaseDate=date(2021, 10, 1), description='Single mother Alex turns to housecleaning to make ends meet as she escapes an abusive relationship and overcomes homelessness to create a better life for her daughter, Maddy.').save()

Show(name='Lupin', releaseDate=date(2021, 1, 8), description='A retelling of the classic French story about Arsène Lupin, the world-famous gentleman thief and master of disguise.').save()

app = Flask(__name__)

@app.route('/shows', methods=['GET', 'POST'])
@app.route('/shows/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
       return jsonify(model_to_dict(Show.get(Show.id == id)))
    else:
        allShows = []
        for show in Show.select():
            allShows.append(model_to_dict(show))
        return jsonify(allShows)

  if request.method == 'PUT':
     body = request.get_json()
     show = Show.update(body).where(Show.id == id)
     show.execute()
     return jsonify({"updated": True})

  if request.method == 'POST':
     new_show = dict_to_model(Show, request.get_json())
     new_show.save()
     return jsonify({"added": True})

  if request.method == 'DELETE':
     removed = Show.delete().where(Show.id == id)
     removed.execute()
     return jsonify({"removed": True})

app.run(port=9000, debug=True)


