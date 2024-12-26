class Films:
    def __init__(self, name=None, genre=None, year=None, rating=None, authors=None, duration=None):
        self.name = name
        self.genre = genre  
        self.year = year
        self.rating = rating
        self.authors = authors
        self.duration = duration


class NodeFilm:
    def __init__(self, data: Films, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


class FilmList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def average_rating(self):
        current = self.head
        total_rating = 0
        count = 0
        while current is not None:
            total_rating += current.data.rating
            count += 1
            current = current.next
        return total_rating / count if count > 0 else 0

    def filter_films_by_year(self, year):
        current = self.head
        while current is not None:
            if current.data.year == year:
                print(f"Title: {current.data.name}, Genre: {current.data.genre}, Year: {current.data.year}, Rating: {current.data.rating}, Authors: {current.data.authors}, Duration: {current.data.duration}")
            current = current.next
        
    def count_by_genre(self):
        current = self.head
        genre_count = {}
        while current is not None:
            if current.data.genre in genre_count:
                genre_count[current.data.genre] += 1
            else:
                genre_count[current.data.genre] = 1
            current = current.next
        return genre_count
    
    def delete_by_name(self, name):
        current = self.head
        while current is not None:
            if current.data.name == name:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def set_rating_by_name(self, name):
        current = self.head
        while current is not None:
            if current.data.name == name:
                new_rating = float(input("Enter new rating: "))
                current.data.rating = new_rating
                return
            current = current.next

    def get_films_by_author(self, author):
        current = self.head
        while current is not None:
            if author in current.data.authors:
                print(f"Title: {current.data.name}, Genre: {current.data.genre}, Year: {current.data.year}, Rating: {current.data.rating}, Authors: {current.data.authors}, Duration: {current.data.duration}")
            current = current.next

    def filter_films_by_duration(self, duration):
        current = self.head
        while current is not None:
            if current.data.duration <= duration:
                print(f"Title: {current.data.name}, Genre: {current.data.genre}, Year: {current.data.year}, Rating: {current.data.rating}, Authors: {current.data.authors}, Duration: {current.data.duration}")
            current = current.next


film1 = Films("Inception", "Sci-Fi", 2010, 8.8, ["Christopher Nolan"], 148)
film2 = Films("The Matrix", "Sci-Fi", 1999, 8.7, ["Lana Wachowski", "Lilly Wachowski"], 136)
film3 = Films("Interstellar", "Sci-Fi", 2014, 8.6, ["Christopher Nolan"], 169)


node1 = NodeFilm(film1)
node2 = NodeFilm(film2)
node3 = NodeFilm(film3)


node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2


film_list = FilmList(head=node1, tail=node3)


print()
print("Films from 1999:")
film_list.filter_films_by_year(1999)
print()

print("Count of films by genre:")
genre_count = film_list.count_by_genre()
print(genre_count)
print()

print("Films by Christopher Nolan:")
film_list.get_films_by_author('Christopher Nolan')
print()

print("Films with duration <= 150 minutes:")
film_list.filter_films_by_duration(150)
print()

print("Films after deleting 'The Matrix':")
film_list.delete_by_name("The Matrix")
film_list.filter_films_by_year(1999)
film_list.filter_films_by_year(2010)
film_list.filter_films_by_year(2014)
print()

print("Average rating after deletion:")
average_rating_after_deletion = film_list.average_rating()
print(average_rating_after_deletion)
print()