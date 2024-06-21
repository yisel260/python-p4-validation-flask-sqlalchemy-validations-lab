from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_email(self, key, name):
        matched_name = Author.query.filter(Author.name == name).first()
        if name:
            matched_name = Author.query.filter(Author.name == name).first()
            if matched_name:
                raise ValueError("author name must be unique")
        else: 
            raise ValueError("author name must be a nonempty string")
        return name
    
    @validates('phone_number')
    def validates_phone_number(self,key,phone_number):
        print("Inside phone_number method")

        if len(phone_number) == 10 and phone_number.isdigit():
            return phone_number
        else:
            raise ValueError("Phone number must be 10 characters")



    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'


class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    @validates('title')
    def validates_title(self,key,title):
        
        if title:
            if title and any(word.lower() in title.lower().strip() for word in ["Won't believe", "Secret", "Top", "Guess"]):
                return title
            else:
                raise ValueError("Title is not clickbaity enough")
        else: 
            raise ValueError ("title must be a none-empty string")
        
  
        
    @validates('content')
    def validates_content(self,key,content):
        if len(content) >= 250:
            return content
        else: 
            raise ValueError ("content must be at least 250 characters")
        
    @validates('summary')
    def validates_summary(self,key,summary):
       
        if len(summary) >= 0 and len(summary) <= 250:
            return summary
        
        else: 
            raise ValueError ("content must be at least 250 characters")
        
    @validates('category')
    def validate_category(self,key,category):
        if category == "Fiction" or category == "Non-Fiction":
            return category
        else: 
            raise ValueError ("category must be either 'Fiction' or 'Non-Fiction'")
    # Add validators  


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
