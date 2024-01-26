class bazi:
    def __init__(self, z):
        self.z = z
        self.board = [[None for _ in range(z)] for _ in range(z)]
        self.players = {0: [], 1: []}
        self.current_player = 0

    def sarbaz_hast(self,soldier_id):
        if soldier_id in [soldier.id for soldier in self.players[self.current_player]]:
            return True
        return False

    def is_position_valid(self,x, y):
        return 0 <= int(x) < self.z and 0 <= int(y) < self.z

    def new_soldier(self,y,soldier_id, x,solider_type):
        if self.sarbaz_hast(soldier_id):
            print("duplicate tag")
            return
        if not self.is_position_valid(x, y):
            print("out of bounds")
            return
        if self.board[x][y] is not None:
            print("duplicate tag")
            return
        soldier = Soldier(soldier_id, x, y,solider_type)
        self.board[x][y] = soldier
        self.players[self.current_player].append(soldier)

    def move_soldier(self, soldier_id, direction):
        if soldier_id not in [soldier.id for soldier in self.players[self.current_player]]:
            print("soldier does not exist")
            return

        for soldier in self.players[self.current_player]:
            if soldier.id == soldier_id:
                current_x, current_y = soldier.x, soldier.y
                if direction == "up":
                    new_x, new_y = current_x - 1, current_y
                elif direction == "down":
                    new_x, new_y = current_x + 1, current_y
                elif direction == "left":
                    new_x, new_y = current_x, current_y - 1
                elif direction == "right":
                    new_x, new_y = current_x, current_y + 1

                if not self.is_position_valid(new_x, new_y):
                    print("out of bounds")
                    return

                if self.board[new_x][new_y] is not None:
                    print("duplicate tag")
                    return

                soldier.x, soldier.y = new_x, new_y
                self.board[new_x][new_y] = soldier
                self.board[current_x][current_y] = None
                break

    def attack(self, attacker_id, target_id):
        attacker = None
        target = None

        for soldier in self.players[self.current_player]:
            if soldier.id == attacker_id:
                attacker = soldier
            elif soldier.id == target_id:
                target = soldier

        if attacker is None or target is None:
            print("soldier does not exist")
            return

        distance = abs(attacker.x - target.x) + abs(attacker.y - target.y)
        if distance > 2:
            print("the target is too far")
            return
        print("target eliminated" if target.health <= 0 else "")
    def info(self, soldier_id):
        for soldier in self.players[self.current_player]:
            if soldier.id == soldier_id:
                print("health: {soldier.health}\nlocation: {soldier.x} {soldier.y}")
                return

        print("soldier does not exist")
    def who_is_in_the_lead(self):
        player_health = {0: 0, 1: 0}

        for player, soldiers in self.players.items():
            for soldier in soldiers:
                player_health[player] += soldier.health

        if player_health[0] > player_health[1]:
            print("Player 0 is in the lead")
        elif player_health[0] < player_health[1]:
            print("Player 1 is in the lead")
        else:
            print("draw")
class Soldier:
    def __init__(self, y,x,soldier_id):
        self.y = y
        self.health = 100
        self.id = soldier_id
        self.x = x
class Melee(Soldier):
    def __init__(self, y,soldier_id, x):
        super().__init__(y,soldier_id,x)
        self.range=1
        self.damage=20
class Archer(Soldier):
    def __init__(self,y,soldier_id, x):
        super().__init__(y,soldier_id, x)
        self.range=2
        self.damage=10
def shoroo():
    a = int(input())
    game = bazi(a)
    while True:
        b = input().split()
        if b[0] == "end":
            break
        if b[0] == "new":
            game.new_soldier(b[1], int(b[2]), int(b[3]), int(b[4]))
        elif b[0] == "who" and b[1] == "is" and b[2] == "in" and b[3] == "the" and b[4] == "lead":
            game.who_is_in_the_lead()
        elif b[0] == "attack":
            game.attack(int(b[1]), int(b[2]))
        elif b[0] == "move":
            game.move_soldier(int(b[1]), b[2])
        elif b[0] == "info":
            game.info(int(b[1]))
shoroo()