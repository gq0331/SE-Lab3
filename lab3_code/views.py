# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 13:51:59 2015

@author: XYRS
"""
from django.shortcuts import  render_to_response
from books.models import Author, Book

#-------------search--------------------------
def search(request):
    if request.GET:
        message = request.GET['q']
        p = Author.objects.filter(Name=message)
        books = Book.objects.filter(AuthorID__Name=message)
        return render_to_response('search_result.html',locals())
    else:
        return render_to_response('search.html')

#-------------search results--------------------------        
def search_results(request):
    BookID = request.GET['id']
    book = Book.objects.get(id=BookID)
    return render_to_response('book_info.html',locals())

#-------------delete one book--------------------------
def delete(request):
    if request.GET:
        ID = request.GET['id']
        book = Book.objects.get(id=ID)
        book.delete()
        return render_to_response('search.html')

#-------------display all the books--------------------------     
def display(request):
    p = Author.objects.all()
    books = Book.objects.all()
    return render_to_response('display.html',locals())
    
        
        
