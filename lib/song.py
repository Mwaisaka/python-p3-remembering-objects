class Song:
    
    all=[]
    
    def __init__(self,name):
        self.name=name
        Song.all.append(self)
    @classmethod
    def add_song_to_all(cls,song):
        cls.all.append(song)
    @classmethod
    def show_song_names(cls):
        print([song.name for song in cls.all])

big_energy=Song("Big Energy")
out_of_touch = Song("Out of Touch")
ninety_nine_problems = Song("99 Problems")
thriller = Song("Thriller")

Song.show_song_names()

class Students:
    master=[]
    def __init__(self,name):
        self.name=name
        Students.master.append(self)
    @classmethod
    def add_student(cls,name):
        cls.master.append(name)
    @classmethod
    def display_student(cls):
        print([student.name for student in cls.master])

student1=Students("Frank")
student2=Students("Kashere")
student3=Students("Mwaisaka")

Students.display_student()