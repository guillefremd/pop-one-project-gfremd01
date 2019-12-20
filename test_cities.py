import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

def test_compute_total_distance2():

    roadmap=[]
    assert compute_total_distance(roadmap)== False

def test_compute_total_distance3():

    roadmap=[("state1", "capi1", -4, 6)]
    assert compute_total_distance(roadmap)== False
   

def test_compute_total_distance4():

    roadmap=[("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755)]
    assert compute_total_distance(roadmap)== False

def test_compute_total_distance5():
    road_map1 = [("Kentucky", "Frankfort", "dsfsdf" , "fdsff"),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    
    assert compute_total_distance(road_map1)==False



def test_swap_cities():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    assert swap_cities(roadmapA, 0, 1)[0]== [("state2", "capi2", 123, 323),("state1", "capi1", 22, 33),("state3", "capi13", 42, 11)]
   


def test_swap_cities2():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    assert swap_cities(roadmapA, 1, 1)== False


def test_swap_cities3():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    assert swap_cities(roadmapA, "a", 1)== False

    
def test_swap_cities4():

    roadmapA=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]
    
    assert swap_cities(roadmapA, 2.4, 1)== False

    
def test_shift_cities():
    
    roadmapB=[("state1", "capi1", 22, 33),("state2", "capi2", 123, 323),("state3", "capi13", 42, 11)]   

    assert shift_cities(roadmapB)==[("state3", "capi13", 42, 11), ("state1", "capi1", 22, 33),("state2", "capi2", 123, 323)]



def test_shift_cities2():
    
    roadmapB=[("state1", "capi1", -4, 6)]
    assert shift_cities(roadmapB)== False
    

    

