import random as rd

class Monstergame:
  def __init__(self):
    self.player_health = 50
    self.monster_health = 50
    self.attempts = 5

  def random_number(self):
      return str(rd.randint(1,3))

  def user_input(self):
    while True:
      try:

        user_number = input('1부터 3 사이의 숫자를 입력하시오.:')

        if int(user_number) >=1 and int(user_number) <=3 :
          return user_number

        elif user_number[0] == ' ' :
          print('\n알맞은 숫자를 입력하시오.\n')
          print('-'*45)
        else :
          print('\n알맞은 숫자를 입력하시오.\n')
          print('-'*45)
      except ValueError:
        print('\n알맞은 숫자를 입력하시오.\n')
        print('-'*45)

  def round(self, user_number):
    
 
    if user_number == self.random_number():
      print('\n정확합니다! monster의 체력을 10 깎습니다.\n')
      
      self.monster_health -= 10
      self.attempts += 1
      self.player_health += 10

    else:
      print('\n틀렸습니다. player의 체력을 10 깎습니다.\n')
      self.player_health -= 10
    self.attempts -= 1
    if self.player_health < 30 or self.attempts < 3 :
      print('\033[31m' +'monster : {}, 내 체력: {}, 남은 시도 횟수: {}\n'.format(self.monster_health, self.player_health, self.attempts) + '\033[0m')
      print('-'*45)
    else :
      print('monster : {}, 내 체력: {}, 남은 시도 횟수: {}\n'.format(self.monster_health, self.player_health, self.attempts))
      print('-'*45)

  def game(self):
    while self.attempts >= 0:
      if self.monster_health == 0:
        print('\n몬스터를 물리쳤습니다! 축하드립니다!')
        break
      if self.player_health == 0:
        print('\n플레이어의 체력이 0이 되어 게임을 종료합니다.')
        break

      if self.attempts == 0 :
        print('\n시도 횟수가 소진되어 게임을 종료합니다.')
        break
      user_number = self.user_input()
      self.round(user_number)


