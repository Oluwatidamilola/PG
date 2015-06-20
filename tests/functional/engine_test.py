import sys
import unittest
from modules.engine import Engine
from tests.helpers import BaseTest

class CanReadStdOutAndMockPrompt(BaseTest):
    def setUp(self):
        self.init()

    def test_can_get_output_from_stdout_and_input_to_stdin(self):
        self.say("Hero")
        engine = Engine(self.fake_input, self.fake_print)
        engine.greet()
        self.assertEqual("Hello, what is your name: ", self.printed[0])
        self.assertEqual("Welcome to text adventure, Hero!", self.printed[1])

class CanLoopTheMainLoop(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.fake_input, self.fake_print)
    
    def test_fred_can_start_and_stop_the_loop_with_ease(self):
        # Fred is an avid gamer, some would say that he is a compulsive gamer
        # It has gotten so bad that he games in the middle of the night, when he should be sleeping
        # He games in the day at work.
        # Sometimes he games when he should be mowing the lawn.
        # Today Fred is trying a new CodeNewbie text adventure game he found, he starts it up
        # As soon as he gets the prompt of the main loop his boss walks by
        # In a panic Fred presses "Q" to quit.
        self.say("Q")
        self.engine.main_loop()
        
        # The text adventure ends 
        self.assertPrinted(">", 0)
<<<<<<< HEAD

    def test_fred_can_stop_the_loop_with_lower_case_q(self):
        # Fred when closing the game as quickly as possible doesn't have time to press shift 
        # He sends a lower case 'q' instead
        # The game closes anyway
        self.say("q")
        self.engine.main_loop()
        
        # The text adventure ends 
        self.assertPrinted(">", 0)
=======
>>>>>>> 376ef97... Creates main loop and allows 'Q' to exit the main loop
