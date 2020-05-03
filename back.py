import json
from settings import *

class Anime:
    with open(alist, "r") as f:
        lists = json.load(f)

    def view_all(self):
        return Anime.lists

    def view(self, title: str):
        return Anime.lists[title]

    def add(self, title: str, ep: float, version: str):
        Anime.lists[title] = {"Ep": ep, "version": version}
    
    def remove(self, title: str):
        del Anime.lists[title]

    def add_ep(self, title: str, nums: float):
        Anime.lists[title]["Ep"] += nums
    
    def sub_ep(self, title: str, nums: float):
        Anime.lists[title]["Ep"] -= nums

    def save(self):
        with open(alist, "w") as f:
            json.dump(Anime.lists, f)


class Manga:
    with open(mlist, "r") as f:
        lists = json.load(f)
    
    def view_all(self):
        return Manga.lists

    def view(self, title: str):
        return Manga.lists[title]

    def add(self, title: str, ch: float):
        Manga.lists[title] = {"Ch": ch}
    
    def remove(self, title: str):
        del Manga.lists[title]

    def add_ep(self, title: str, nums: float):
        Manga.lists[title]["Ch"] += nums
    
    def sub_ep(self, title: str, nums: float):
        Manga.lists[title]["Ch"] -= nums

    def save(self):
        with open(mlist, "w") as f:
            json.dump(Manga.lists, f)


class Webtoon:
    
    with open(wlist, "r") as f:
        lists = json.load(f)

    def view_all(self):
        return Webtoon.lists

    def view(self, title: str):
        return Webtoon.lists[title]

    def add(self, title: str, Ep:float):
        Webtoon.lists[title] = {"Ep": Ep}
    
    def remove(self, title: str):
        del Webtoon.lists[title]

    def add_ep(self, title: str, nums: float):
        Webtoon.lists[title]["Ep"] += nums
    
    def sub_ep(self, title: str, nums: float):
        Webtoon.lists[title]["Ep"] -= nums

    def save(self):
        with open(wlist, "w") as f:
            json.dump(Webtoon.lists, f)


if __name__ == "__main__":
    Anime().add("Pokemon", "Dub")
    print(Anime().view_all())
    Anime().save()
    Manga().add("That time I reincarnated as a slime")
    print(Manga().view_all())
    Manga().save()
    Webtoon().add("Winter Moon")
    print(Webtoon().view_all())
    Webtoon().save()
    