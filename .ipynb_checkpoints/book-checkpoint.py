{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "be52339e-be59-40a7-970c-37d7e5966ce8",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Book:\n",
    "    def __init__(self, title, price, availability, rating):\n",
    "        self.title = title\n",
    "        self.price = price\n",
    "        self.availability = availability\n",
    "        self.rating = rating\n",
    "\n",
    "    def to_dict(self):\n",
    "        return {\n",
    "            \"title\": self.title,\n",
    "            \"price\": self.price,\n",
    "            \"availability\": self.availability,\n",
    "            \"rating\": self.rating\n",
    "        }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e3cacac4-7cde-4de8-802e-64226d78f2cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'title': 'Vagabond', 'price': 10.99, 'availability': 'In stock', 'rating': 'Three'}\n"
     ]
    }
   ],
   "source": [
    "book = Book(\"Vagabond\", 10.99, \"In stock\", \"Three\")\n",
    "print(book.to_dict())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b874bd1-b4b1-4967-893e-1edcd8f41cf9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
