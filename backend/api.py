
from flask_restful import Resource, Api
from flask import Flask, jsonify, request, make_response
import jwt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from functools import wraps
from models import *


class Login(Resource):
      
    # Corresponds to POST request
    def post(self):
          
        username = request.json["username"]
        password = request.json["password"]

        user = db.session.query(User).filter(User.username == username,User.password == password).first()
    
        formattedUser = {
            'id': user.id,
            'name': user.username, 
            'email': user.email
        }
        if user:
            access_token = create_access_token(identity=user.id)
            return make_response(jsonify({'message':"Login Succeeded!", 'access_token':access_token, 'user': formattedUser}),200)
        else:
            return make_response(jsonify({'message':"Bad Email or Password"}),401)
                
        
class Register(Resource):
    def post(self):
        
        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]
        
        new_user = User(username=username, password=password, email=email)
        try:
            # msg = "Hi " + username + ", you are successfully registered!!"
            db.session.add(new_user)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"Register Succeeded!"}),200)
    
class Decks(Resource):
    @jwt_required()
    def get(self):
        
        current_user_id = get_jwt_identity()
        
        print("Current user:", current_user_id)
        decks = db.session.query(Deck).filter(Deck.user_id == current_user_id).all()
        
        formattedDecks = []
        for d in decks:
            formattedDecks.append({
                'id': d.id,
                'name': d.name,
                'last_reviewed': d.last_reviewed,
                'score': d.score
        })
          
        print("Formatted Decks:", formattedDecks)
        return make_response(jsonify(formattedDecks), 200)
    
    @jwt_required()
    def post(self):
        
        current_user_id = get_jwt_identity()
        
        name = request.get_json()["deck_name"] 
        
        new_deck = Deck(name=name,user_id=current_user_id)
        try:
            db.session.add(new_deck)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"New Deck added successfully!"}),200)
    
    @jwt_required()
    def delete(self):
        current_user_id = get_jwt_identity()
        
        deck_id = request.get_json()["deck_id"] 
        deck = Deck.query.get(deck_id)
        
        try:
            db.session.delete(deck)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"Deck deleted successfully!"}),200)
    
class Cards(Resource):
    @jwt_required()
    def get(self):
        deck_id = request.json["deck_id"]
        
        cards = db.session.query(Card).filter(Card.deck_id == deck_id).all()
        
        formattedCards = []
        for c in cards:
            formattedCards.append({
                'id': c.id,
                'front': c.front,
                'back': c.back
        })
                
        return make_response(jsonify(formattedCards),200)
    
    @jwt_required()
    def post(self):
        
        front = request.json["front"]
        back = request.json["back"]
        deck_id = request.json["deck_id"]
        
        try:
            new_card = Card(front=front,back=back,deck_id=deck_id)
            db.session.add(new_card)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"New Card added successfully!"}),200)
    
    @jwt_required()
    def delete(self):
        
        card_id = request.get_json()["card_id"] 
        card = Card.query.get(card_id)
        
        try:
            db.session.delete(card)
            db.session.commit()
        except:
            raise
        
        return make_response(jsonify({'message':"Card deleted successfully!"}),200)
    
        
    
        
        
        
        
        
    

        
        
        
    
        
        
        
        
        
        