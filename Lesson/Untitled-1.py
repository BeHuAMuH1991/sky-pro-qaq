from user import User
from card import Card

user1  = User("Alex")
user1.sayName()
user1.setAge(21)
user1.sayAge()


card = Card("1234 1234 1234 1234", "03/99", "Alex F")
user1.addCard(card)
user1.getCard().pay(1000)






