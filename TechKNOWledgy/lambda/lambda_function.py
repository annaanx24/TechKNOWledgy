# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import os
import boto3

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_dynamodb.adapter import DynamoDbAdapter
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

from readFromDynamo import read_ddb

"""
ddb_region = os.environ.get('DYNAMODB_PERSISTENCE_REGION')
ddb_table_name = os.environ.get('DYNAMODB_PERSISTENCE_TABLE_NAME')

ddb_resource = boto3.resource('dynamodb', region_name=ddb_region)
dynamodb_adapter = DynamoDbAdapter(table_name=ddb_table_name, create_table=False, dynamodb_resource=ddb_resource)
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
inputs = {}


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to Tech-KNOWledgy! What is your name?"
        reprompt_text = "My name is Alexa, what is your name?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )


class CaptureUserNameIntentHandler(AbstractRequestHandler):
    """Handler for Capture Name Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureUserNameIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        name = slots["name"].value
        inputs["name"] = name
        print(name)
        speak_output = 'Hi {name}, are you in elementary school, middle school, high school, or college? Choose one.'.format(name=name)
        reprompt_text = "Are you in elementary school, middle school, high school, or college? Choose one."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )
        
    
class CaptureUserAgeIntentHandler(AbstractRequestHandler):
    """Handler for Capture Age Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureUserAgeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        age = slots["age"].value
        inputs["age"] = age
        print(age)
        speak_output = 'So you\'re in {age}. What gender do you identify with? Or say skip.'.format(age=age)
        reprompt_text = "What gender are you?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )

class CaptureUserGenderIntentHandler(AbstractRequestHandler):
    """Handler for Capture Gender Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureUserGenderIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        gender = slots["gender"].value
        inputs["gender"] = gender
        print(gender)
        speak_output = 'I got that you are a {gender}. What race do you identify with? Or say skip.'.format(gender=gender)
        reprompt_text = "What is your race?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )
    
class CaptureUserRaceIntentHandler(AbstractRequestHandler):
    """Handler for Capture Race Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureUserRaceIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        race = slots["race"].value
        inputs["race"] = race
        print(race)
        speak_output = 'Got it! Are you looking for a mentorship, scholarship, learning, or internship? Choose one.'.format(race=race)
        reprompt_text = "Are you looking for a mentorship, scholarship, learning, or internship? Choose one."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )
    
class CaptureUserOppIntentHandler(AbstractRequestHandler):
    """ Handler for Capture Opportunity Intent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureUserOppIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        opportunity = slots["opportunity"].value
        inputs["opportunity"] = opportunity
        print(opportunity)
        # items = read_ddb(inputs)
        speak_output = 'I found three amazing opportunities for you! #1 Amazon Future Engineer Scholarship. #2 The ExpressVPN Future of Privacy Scholarship. #3 FIRST Robotics Scholarship. Would you like me to save any of those for you?'.format(opportunity=opportunity)
        logger.info(inputs)
        
        """
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.persistent_attributes
        if not attr:
            attr['counter'] = 0
            attr['state'] = 'ENDED'

        handler_input.attributes_manager.session_attributes = attr

        handler_input.attributes_manager.save_persistent_attributes()
        
        """
        
        # type: (HandlerInput) -> Response
        # session_attr = handler_input.attributes_manager.session_attributes
        # session_attr['state'] = "STARTED"
        # session_attr["counter"] += 1
        # handler_input.attributes_manager.persistent_attributes = session_attr
        # handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class CaptureUserSaveIntentHandler(AbstractRequestHandler):
    """ Handler for Capture Opportunity Intent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureUserSaveIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # slots = handler_input.request_envelope.request.intent.slots
        # answer = slots["answer"].value

        # items = read_ddb(inputs)
        speak_output = 'Great! I saved #1 Amazon Future Engineer Scholarship. Say your name for more opportunities or say Get My opportunities'
        logger.info(inputs)
        
        """
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.persistent_attributes
        if not attr:
            attr['counter'] = 0
            attr['state'] = 'ENDED'

        handler_input.attributes_manager.session_attributes = attr

        handler_input.attributes_manager.save_persistent_attributes()
        
        """
        
        # type: (HandlerInput) -> Response
        # session_attr = handler_input.attributes_manager.session_attributes
        # session_attr['state'] = "STARTED"
        # session_attr["counter"] += 1
        # handler_input.attributes_manager.persistent_attributes = session_attr
        # handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
class GetOppIntentHandler(AbstractRequestHandler):
    """ Handler for Capture Opportunity Intent. """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetOppIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # slots = handler_input.request_envelope.request.intent.slots
        # answer = slots["answer"].value

        # items = read_ddb(inputs)
        speak_output = 'You have one opportunity. #1 Amazon Future Engineer Scholarship with a deadline in January 2022'
        logger.info(inputs)
        
        """
        # type: (HandlerInput) -> Response
        attr = handler_input.attributes_manager.persistent_attributes
        if not attr:
            attr['counter'] = 0
            attr['state'] = 'ENDED'

        handler_input.attributes_manager.session_attributes = attr

        handler_input.attributes_manager.save_persistent_attributes()
        
        """
        
        # type: (HandlerInput) -> Response
        # session_attr = handler_input.attributes_manager.session_attributes
        # session_attr['state'] = "STARTED"
        # session_attr["counter"] += 1
        # handler_input.attributes_manager.persistent_attributes = session_attr
        # handler_input.attributes_manager.save_persistent_attributes()

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()
# sb = CustomSkillBuilder(persistence_adapter = dynamodb_adapter)

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureUserNameIntentHandler())
sb.add_request_handler(CaptureUserAgeIntentHandler())
sb.add_request_handler(CaptureUserGenderIntentHandler())
sb.add_request_handler(CaptureUserRaceIntentHandler())
sb.add_request_handler(CaptureUserOppIntentHandler())
sb.add_request_handler(CaptureUserSaveIntentHandler())
sb.add_request_handler(GetOppIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()