class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.word_list = []
        for word in self.title.split():
            self.word_list.append(word)
        for word in self.contents.split():
            self.word_list.append(word)

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        
        return len(self.title.split()) + len(self.contents.split())

    def reading_time(self, wpm):
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        string_to_read = " ".join(self.word_list[0:words_can_read])
        del self.word_list[0:words_can_read]
        return string_to_read