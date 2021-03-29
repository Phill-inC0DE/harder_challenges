#BUILDS A DICTIONARY OF PLAYERS, RECORDS WORDS FOR EACH PLAYER AND PRINTS OUT FINAL SCORES.

upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_to_points = {key:value for key, value in zip(upper_letters, points)}
lower_letter_points = {key:value for key, value in zip(lower_letters, points)}
letter_to_points.update(lower_letter_points)
#print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points.get(letter, 0)
  return point_total
brownie_points = score_word("BROWNIE")
#print(brownie_points)
#prints: 15

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points
#print(player_to_points)
#prints: {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31}

#FURTHER PRACTICE:
#TASK1
#play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played.
def play_word(player, word):
  if player not in player_to_words.keys():
    player_to_words[player] = [word]
  else:
    values = player_to_words.get(player)
    values.append(word)
  return player_to_words

play_word("Phil", "DONKEY")
play_word("Kez", "MONKEY")
play_word("Phil", "LION")
play_word("Kez", "PARROT")
play_word("Phil", "Kangaroo")
#print(player_to_words)
#prints: {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD'], 'Phil': ['DONKEY', 'LION', 'Kangaroo'], 'Kez': ['MONKEY', 'PARROT']}


#TASK2
#update_point_totals() — turn your nested loops into a function
#that you can call any time a word is played
def update_point_totals(players):
  for player, words in players.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points
  return player_to_points
#print(update_point_totals(player_to_words))
#prints: {'player1': 29, 'wordNerd': 32, 'Lexi Con': 31, 'Prof Reader': 31, 'Phil': 40, 'Kez': 26}

#TASK3
#make your letter_to_points dictionary able to handle
#lowercase inputs as well.
#COMPLETED CHECK AT BEGINNING OF CODE.