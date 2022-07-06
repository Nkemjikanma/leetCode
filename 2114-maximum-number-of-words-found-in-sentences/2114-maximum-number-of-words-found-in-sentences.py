class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = 0
        for sentence in sentences:
            sentence = sentence.split(" ")
            if len(sentence) > words:
                words = len(sentence)
        return words
        