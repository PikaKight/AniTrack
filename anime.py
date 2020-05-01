class Anime:
    anime_list = {}

    def view_all(self):
        return Anime.anime_list

    def view(self, anime: str):
        return Anime.anime_list[anime]
    
    def add_new(self, anime: str):
        Anime.anime_list[anime] = {"Ep": 0}
    
    def add_episode(self, anime: str, num: int):
        Anime.anime_list[anime]["Ep"] += num

    def remove(self, anime: str):
        
        

