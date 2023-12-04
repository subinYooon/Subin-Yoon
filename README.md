# Subin-Yoon

## Monster Game

#### Monster game은 몬스터가 가진 랜덤한 숫자를 맞추어 몬스터를 잡는 게임입니다.


### Set UP

1. Monster의 기본 체력은 50입니다.

2. Player의 기본 체력은 50입니다. 

3. 기본 시도 기회는 5번입니다. 

4. 랜덤 숫자는 1에서 3사이입니다. 숫자는 항상 랜덤입니다.

### Play

1.  1부터 3사이의 숫자 중 하나를 입력합니다.
   
2. 숫자를 틀린다면 시도 기회 -1과 Player의 체력 -10이 됩니다.

3. 숫자를 맞춘다면 시도 기회 +2와 Monster의 체력 -10, Player의 체력 +10을 해 줍니다.

4. 만약 체력이 20 이하이거나 시도 횟수가 2 이하이면 안내 글자가 빨간색으로 변하며 경고를 줍니다.

### End

1. Monster의 체력이 0이 된다면 Player의 승리입니다.

2. Player의 체력이 0이 되거나 시도 기회가 0이 된다면 Monster의 승리입니다.
