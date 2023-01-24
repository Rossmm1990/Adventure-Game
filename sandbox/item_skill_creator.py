class Skills:
    def __init__(
        self, skill_name, skill_dmg, skill_type, skill_passive, skill_description
    ):

        self.skill_name = skill_name  # "string"
        self.skill_dmg = skill_dmg  # 0 - infinity
        self.skill_type = skill_type  # "melee" or "ranged"
        self.skill_passive = skill_passive
        self.skill_description = skill_description


class Item:
    def __init__(self, name, item_type, item_dmg, special, item_description):
        self.name = name
        self.name = item_type
        self.item_dmg = item_dmg
        self.item_special = special


sword = Item(
    "sword",
    "m",
    5,
    "b",
    "basic sword does 5 dmg with %10 on hit bleed effect which does an extra 5 dmg per turn",
)
axe = Item("axe", "m", 10, "n", "basic axe does 5 dmg with no special effects")
bow = Item("bow", "r", 5, "n", "basic bow that does 5 dmg")

melee_attack = Skills(
    "melee attack", 5, "m", "n", "basic attack requires melee weapon and does 5 dmg"
)

ranged_attack = Skills(
    "ranged attack", 5, "r", "n", "basic attack requires ranged weapon and does 5 dmg"
)

rend = Skills(
    "rend",
    5,
    "m",
    "b",
    "melee attack that adds bleed effect which does an extra 5 dmg per turn",
)

Master_item_dict = {"sword": sword(), "axe": axe(), "bow": bow()}

Master_skills_dict = {
    "melee_attack": melee_attack(),
    "ranged_attack": ranged_attack(),
    "rend": rend(),
}
