#  Chapter 3 - Python Data Structures (EASY EXAMPLES)

# -------------------------
# 1️ LISTS - creation & indexing
# -------------------------
print("\n--- LISTS ---")
fav_movies = ["Gajni", "PK", "3 Idiots", "Squid Game", "Shan"]

print("All movies:", fav_movies)
print("First movie:", fav_movies[0])      # indexing
print("Third movie:", fav_movies[2])      # indexing
print("Last movie:", fav_movies[-1])      # negative indexing
print("First 3 movies:", fav_movies[:3])  # slicing

# -------------------------
# 2 LIST METHODS
# -------------------------
print("\n--- LIST METHODS ---")
fav_movies.append("Open")          # add at end
print("After append:", fav_movies)

fav_movies.insert(2, "New Insert")  # add at specific position
print("After insert:", fav_movies)

fav_movies.remove("New Insert")    # remove by value
print("After remove:", fav_movies)

fav_movies.pop()                   # remove last
print("After pop:", fav_movies)

fav_movies.sort()                  # sort alphabetically
print("After sort:", fav_movies)

fav_movies.reverse()               # reverse the list
print("After reverse:", fav_movies)

# -------------------------
# 3️ NESTED LISTS
# -------------------------
print("\n--- NESTED LISTS ---")
nested_list = [
    ["Apple", "Banana", "Mango"],     # fruits list
    ["Carrot", "Potato", "Tomato"]    # vegetables list
]

print("Nested list:", nested_list)
print("First inner list:", nested_list[0])
print("Second item of second list:", nested_list[1][1])  # Potato

# -------------------------
# 4️ LOOPS with LISTS
# -------------------------
print("\n--- LOOP THROUGH LIST ---")
for movie in fav_movies:
    print("I like:", movie)

# -------------------------
# 5️ TUPLES (immutable)
# -------------------------
print("\n--- TUPLES ---")
fav_tuple = ("Apple", "Banana", "Mango")
print("Tuple example:", fav_tuple)
print("First fruit in tuple:", fav_tuple[0])
# fav_tuple[0] = "Orange"  #  ERROR: tuples cannot be changed

# -------------------------
# 6️ LEN FUNCTION
# -------------------------
print("\n--- LENGTH ---")
print("Total movies:", len(fav_movies))
print("Total fruits in tuple:", len(fav_tuple))

# -------------------------
# 7️ MUTABLE vs IMMUTABLE
# -------------------------
print("\n--- MUTABLE vs IMMUTABLE ---")
fav_movies[0] = "Ghajini"  # allowed for lists
print("List after change:", fav_movies)

# fav_tuple[0] = "Orange"  #  NOT allowed for tuples
print("Tuple cannot be changed, still:", fav_tuple)
