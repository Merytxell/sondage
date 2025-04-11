# Compte-rendu : Shell Django

## Exercice 2.5 :
On ne peut pas se connecter avec un compte user.

## Exercice 2.6 :
il faut passer l'utilisateur en "statut d'équipe" pour qu'il puisse se connecter, il peut rien faire d'autre.

## Exercice 2.7 :
il faut cocher sur la case "utilisateur actif"

## Excercises 2.2.2

Lister tous les objets de type Question :
```
>>> q = Question.objects.all()
>>> for question in q:
...     print(question.id, question.question_text, question.pub_date)
...
1 What's up? 2025-04-04 09:27:53.778536+00:00
2 quelle saison préférez vous ? 2025-04-04 09:49:03+00:00
3 quel est votre langage préféré ? 2025-04-05 10:00:00+00:00
4 avez vous un animal ? 2025-04-06 16:00:00+00:00
5 Avez-vous déjà visité l'Italie 2025-04-17 04:00:00+00:00
6 Que préférez vous comme sucrerie ? 2025-04-09 09:54:05+00:00
```

Ajoutez un filtre sur la date de publication

```
>>> questions_avril = Question.objects.filter(pub_date__year=2025, pub_date__month=4)
>>> for question in questions_avril:
...     print(question.id, question.question_text, question.pub_date)
...
1 What's up? 2025-04-04 09:27:53.778536+00:00
2 quelle saison préférez vous ? 2025-04-04 09:49:03+00:00
```

Affichez les valeurs de tous les attributs et tous les choix associés.

Afficher id2 :
```
q2 = Question.objects.get(id=2)
>>> print(q2.id, q2.question_text, q2.pub_date)
2 quelle saison préférez vous ? 2025-04-04 09:49:03+00:00
```

Afficher les choix :
```
>>> for choice in q2.choice_set.all():
...     print(choice.id, choice.choice_text, choice.votes)
...
4 Hiver 0
5 printemps 0
6 été 0
7 automne 0
```

Boucle pour afficher les attributs de chaque question et leurs choix associés.
```
questions = Question.objects.all()         
>>> for question in questions:
...     print(f"Question {question.id} : {question.question_text} (publiée le {question.pub_date})")
...     for choice in question.choice_set.all():
...             print(f"  - Choix {choice.id} : {choice.choice_text} (votes : {choice.votes})")
...     print()
...
Question 1 : What's up? (publiée le 2025-04-04 09:27:53.778536+00:00)
  - Choix 1 : Not much (votes : 0)
  - Choix 2 : The sky (votes : 0)

Question 2 : quelle saison préférez vous ? (publiée le 2025-04-04 09:49:03+00:00)
  - Choix 4 : Hiver (votes : 0)
  - Choix 5 : printemps (votes : 0)
  - Choix 6 : été (votes : 0)
  - Choix 7 : automne (votes : 0)

Question 3 : quel est votre langage préféré ? (publiée le 2025-04-05 10:00:00+00:00)
  - Choix 8 : java (votes : 0)
  - Choix 9 : python (votes : 0)

Question 4 : avez vous un animal ? (publiée le 2025-04-06 16:00:00+00:00)
  - Choix 10 : oui (votes : 0)
  - Choix 11 : non (votes : 0)

Question 5 : Avez-vous déjà visité l'Italie (publiée le 2025-04-17 04:00:00+00:00)
  - Choix 12 : oui (votes : 0)
  - Choix 13 : non (votes : 0)

Question 6 : Que préférez vous comme sucrerie ? (publiée le 2025-04-09 09:54:05+00:00)
  - Choix 14 : Le chocolat (votes : 0)
  - Choix 15 : Les bonbons (votes : 0)
  - Choix 16 : Je préfère le salé (votes : 0)
```

Affichez le nombre de choix enregistrés pour chaque question.
```
questions = Question.objects.all()
>>> for question in questions:
...     print(f"Question {question.id} : {question.question_text} a {question.choice_set.count()} choix.")
...
Question 1 : What's up? a 2 choix.
Question 2 : quelle saison préférez vous ? a 4 choix.
Question 3 : quel est votre langage préféré ? a 2 choix.
Question 4 : avez vous un animal ? a 2 choix.
Question 5 : Avez-vous déjà visité l'Italie a 2 choix.
Question 6 : Que préférez vous comme sucrerie ? a 3 choix.
```

Questions par ordre antéchronologique :
```
>>> questions_a = Question.objects.all().order_by('-pub_date')
>>> for question in questions_a:
...     print(question.id, question.question_text, question.pub_date)
...
5 Avez-vous déjà visité l'Italie 2025-04-17 04:00:00+00:00
6 Que préférez vous comme sucrerie ? 2025-04-09 09:54:05+00:00
4 avez vous un animal ? 2025-04-06 16:00:00+00:00
3 quel est votre langage préféré ? 2025-04-05 10:00:00+00:00
2 quelle saison préférez vous ? 2025-04-04 09:49:03+00:00
1 What's up? 2025-04-04 09:27:53.778536+00:00
```

Créer une question :
```
>>> from django.utils import timezone
>>> new_question = Question(question_text="Quelle est ta couleur préférée ?", pub_date=timezone.now())
>>> new_question.save()
>>>     print(new_question.id, new_question.question_text, new_question.pub_date)
        print(new_question.id, new_question.question_text, new_question.pub_date)
>>> print(new_question.id, new_question.question_text, new_question.pub_date)     
7 Quelle est ta couleur préférée ? 2025-04-08 08:33:15.012061+00:00
```

Créer des réponses :
```
>>> from polls.models import Choice
>>> choice1 = Choice(question=new_question, choice_text="Rouge", votes=3)      
>>> choice1.save()
>>> choice2 = Choice(question=new_question, choice_text="Bleu", votes=4) 
>>> choice2.save()                                                       
>>> choice3 = Choice(question=new_question, choice_text="Vert", votes=6)  
>>> choice3.save()
>>> for choice in new_question.choice_set.all():
...     print(choice.choice_text, choice.votes)
...
Rouge 3
Bleu 4
Vert 6
```

Liste des questioons publiées récemment :
```
>>> from django.utils import timezone
>>> recent_questions = Question.objects.filter(pub_date__gte=timezone.now()).order_by('-pub_date')
>>> for question in recent_questions:
...     print(question.id, question.question_text, question.pub_date)
...
5 Avez-vous déjà visité l'Italie 2025-04-17 04:00:00+00:00
6 Que préférez vous comme sucrerie ? 2025-04-09 09:54:05+00:00
7 Quelle est ta couleur préférée ? 2025-04-08 08:33:15.012061+00:00
4 avez vous un animal ? 2025-04-06 16:00:00+00:00
3 quel est votre langage préféré ? 2025-04-05 10:00:00+00:00
2 quelle saison préférez vous ? 2025-04-04 09:49:03+00:00
1 What's up? 2025-04-04 09:27:53.778536+00:00
```
