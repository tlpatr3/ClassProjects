import random

tarot_cards = {
    0:  ("The Fool", "Beginnings, innocence, spontaneity, a free spirit."),
    1:  ("The Magician", "Power, skill, concentration, action, resourcefulness."),
    2:  ("The High Priestess", "Intuition, higher powers, mystery, subconscious mind."),
    3:  ("The Empress", "Femininity, beauty, nature, nurturing, abundance."),
    4:  ("The Emperor", "Authority, structure, control, father figure."),
    5:  ("The Hierophant", "Spiritual wisdom, tradition, conformity, morality."),
    6:  ("The Lovers", "Love, harmony, relationships, choices, alignment of values."),
    7:  ("The Chariot", "Control, willpower, victory, determination."),
    8:  ("Strength", "Courage, patience, inner strength, compassion."),
    9:  ("The Hermit", "Soul-searching, introspection, being alone, inner guidance."),
    10: ("Wheel of Fortune", "Change, cycles, inevitable fate, luck."),
    11: ("Justice", "Fairness, truth, law, cause and effect, clarity."),
    12: ("The Hanged Man", "Pause, surrender, letting go, new perspectives."),
    13: ("Death", "Transformation, endings, transitions, new beginnings."),
    14: ("Temperance", "Balance, moderation, patience, purpose."),
    15: ("The Devil", "Bondage, addiction, materialism, playfulness, temptation."),
    16: ("The Tower", "Sudden change, upheaval, chaos, revelation."),
    17: ("The Star", "Hope, inspiration, spirituality, renewal."),
    18: ("The Moon", "Illusions, fear, anxiety, the subconscious, intuition."),
    19: ("The Sun", "Success, positivity, vitality, warmth, joy."),
    20: ("Judgment", "Reflection, reckoning, awakening, renewal."),
    21: ("The World", "Completion, fulfillment, wholeness, travel."),
}


def draw_tarot_card():
    number = random.randint(0, 21)
    card_name, meaning = tarot_cards[number]
    return f"Your card is {card_name} ({number}): {meaning}"


if __name__ == "__main__":
    print(draw_tarot_card())