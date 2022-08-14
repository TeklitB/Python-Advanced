class LuxuryWatch:
    __watches_created = 0
    
    def __init__(self):
        LuxuryWatch.__watches_created += 1
        self.engrave_text = ''
    
    @classmethod
    def get_number_of_watches_created(cls, eng_txt):
        try:
            LuxuryWatch.validate_engrave_text(eng_txt)
            _luxuryWatch = cls()
            _luxuryWatch.engrave_text = eng_txt
        except Exception as ex:
            print(ex)
        
        return LuxuryWatch.__watches_created
    
    @staticmethod
    def validate_engrave_text(eng_text: str):
        if len(eng_text) > 40 or not eng_text.isalnum():
            raise Exception("The engraving text is invalid")


lw1 = LuxuryWatch()

lw1 = LuxuryWatch.get_number_of_watches_created("silverwatch")

lw1 = LuxuryWatch.get_number_of_watches_created("foo@baz.com")

print(LuxuryWatch.get_number_of_watches_created("foo"))