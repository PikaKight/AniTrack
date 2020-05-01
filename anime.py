class Anime:
    anime_list = {}

    def view(self, anime: str):
        return Anime.anime_list[anime]
    
    def add_new(self, anime: str):
        Anime.anime_list[anime] = {}
    
    def add_episode(self, anime: str, num: int):
        Anime.anime_list[anime]["Ep"] += nums
        

Anime().add_new("SAO")
Anime().add_episode("SAO", 20)
print(Anime().view())