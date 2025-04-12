class Cats:
    def __init__(self, entries):
        self._items = []
        self._lookup = {} 
        for name, value in entries:
            self._items.append(value)
            self._lookup[name] = value
            setattr(self, name, value)

    def __getitem__(self, index):
        return self._items[index]
    

cat = Cats([
    ('owo', '\n\n|\\_ _ _/|\n| o w o|'),
    ('o_o', '\n\n|\\_ _ _/|\n| o _ o |'),
    ('uwu', '\n\n|\\_ _ _/|\n| u w u|'),
    ('x_x', '\n\n|\\_ _ _/|\n| X _ X |'),
    ('OwO', '\n\n|\\_ _ _/|\n| 0 W 0|'),
    ('QwQ', '\n\n|\\_ _ _/|\n|Q W Q|'),
    ('AwA', '\n\n|\\_ _ _/|\n| ^ W ^ |'),
    ('u_u', '\n\n|\\_ _ _/|\n| U _ U |'),
    ('t_t', '\n\n|\\_ _ _/|\n| T _ T |'),
    ('hello', '\n\n|\\_ _ _/|\n| o w o| づ'),
    ('schedule', '\n\n    |\\_ _ _/|\nฅ | o w o | ฅ'),
    ('laptop', '\n\n|\\_ _ _/|\n|   - w - |  _/7'),
    ('shame', '\n\n/|_ _ _|\\ <--- *стыдно*'),
])