import random as rd

class Monstergame:
  ## 게임은 플레이어와 몬스터가 각각 50의 체력과 5번의 시도 기회로 시작됨
  def __init__(self):
    self.player_health = 50
    self.monster_health = 50
    self.attempts = 5

  ## random_number 메서드는 몬스터가 생각한 1부터 3까지의 무작위 숫자를 생성함
  def random_number(self):
      return rd.randint(1,3)

  ## user_input 메서드는 사용자로부터 1부터 3까지의 숫자를 입력받을 때까지 계속해서 입력을 요청함
  def user_input(self):
    ## 무한 루프 : 이 부분은 사용자가 유효한 입력을 제공할 때까지 계속해서 사용자에게 입력을 요청함
    while True:

      ## 유효성 검사
      # try 블록 내에서는 사용자의 입력을 정수로 변환하려 시도함
      # 만약 입력이 정수가 아니라면 (ValueError 예외가 발생하면), except 블록으로 이동함
      try:
        player_number = int(input('1부터 3 사이의 숫자를 입력하시오.:'))

        ## 정상적인 입력 확인
        # 정상적으로 정수로 변환되었다면, 이 값이 1과 3 사이에 있는지 확인
        # 만약 그렇다면, 해당 값을 반환하고 함수를 종료함
        if player_number >=1 and player_number <=3 :
          return player_number

        # 위의 모든 조건을 만족하지 않는 경우, 사용자에게 올바른 입력을 하도록 안내함
        else :
          print('\n알맞은 숫자를 입력하시오.\n')
          print('-'*45)
      except ValueError:
        print('\n알맞은 숫자를 입력하시오.\n')
        print('-'*45)

  def round(self, player_number):

    # 라운드가 시작하면 모든 경우에서 시도 기회를 1 감소
    self.attempts -= 1

    # 만약 사용자가 입력한 숫자와 몬스터가 생각한 숫자가 일치한다면
    # 몬스터의 체력을 10 감소, 시도 기회를 2 증가, 플레이어의 체력을 10 증가시킴
    if player_number == self.random_number():
      print('\n정확합니다! monster의 체력을 10 깎습니다.\n')
      self.monster_health -= 10
      self.attempts += 2
      self.player_health += 10

    # 일치하지 않는다면
    # 플레이어의 체력을 10 감소
    else:
      print('\n틀렸습니다. player의 체력을 10 깎습니다.\n')
      self.player_health -= 10


    ## 게임 상태 출력
    # 만약 플레이어의 체력이 30보다 작거나 시도 기회가 3보다 작으면 게임 상태를 빨간색으로 출력
    # 그렇지 않으면 일반적인 출력
    if self.player_health < 30 or self.attempts < 3 :
      print('\033[31m' +'monster : {}, 내 체력: {}, 남은 시도 횟수: {}\n'\
            .format(self.monster_health, self.player_health, self.attempts) + '\033[0m')
      print('-'*45)
    else :
      print('monster : {}, 내 체력: {}, 남은 시도 횟수: {}\n'\
            .format(self.monster_health, self.player_health, self.attempts))
      print('-'*45)

  ## 게임 루프
  def game(self):
    while self.attempts >= 0:
      # 몬스터의 체력이 0인 경우
      # 플레이어가 몬스터를 물리쳤다는 메시지를 출력하고 break를 통해 게임 루프를 종료
      if self.monster_health == 0:
        print('\n몬스터를 물리쳤습니다! 축하드립니다!')
        break

      # 플레이어의 체력이 0인 경우
      # 플레이어가 패배했다는 메시지를 출력하고 break를 통해 게임 루프를 종료
      if self.player_health == 0:
        print('\n플레이어의 체력이 0이 되어 게임을 종료합니다.')
        break

      # 시도 횟수가 0인 경우
      # 시도 기회가 모두 소진되었다는 메시지를 출력하고 break를 통해 게임 루프를 종료
      if self.attempts == 0 :
        print('\n시도 횟수가 소진되어 게임을 종료합니다.')
        break

      # 사용자 입력 받기
      # 게임 루프에서는 매 라운드마다 사용자로부터 숫자를 입력 받음
      player_number = self.user_input()

      # 라운드 실행
      # 사용자가 입력한 숫자를 가지고 round 메서드를 호출하여 게임 라운드를 실행함
      self.round(player_number)


