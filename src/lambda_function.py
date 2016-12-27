"""
"""

from __future__ import print_function

obj_pep_text = {}
obj_pep_text['1'] = "PEP stands for Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature. " + \
                    "We intend PEPs to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions. " + \
                    "Because the PEPs are maintained as text files in a versioned repository, their revision history is the historical record of the feature proposal."
obj_pep_text['4'] = "PEP 4 - Deprecation of Standard Modules. When new modules were added to the standard Python library in the past, it was not possible to foresee whether they would still be useful in the future. Even though Python Comes With Batteries Included, batteries may discharge over time. " + \
                    "Carrying old modules around is a burden on the maintainer, especially when there is no interest in the module anymore. At the same time, removing a module from the distribution is difficult, as it is not known in general whether anybody is still using it. " + \
                    "This PEP defines a procedure for removing modules from the standard Python library. Usage of a module may be 'deprecated', which means that it may be removed from a future Python release. The rationale for deprecating a module is also collected in this PEP. If the rationale turns out faulty, the module may become 'undeprecated'."
obj_pep_text['5'] = "PEP 5 - Guidelines for Language Evolution. These guidelines apply to future versions of Python that introduce backward-incompatible behavior. Backward incompatible behavior is a major deviation in Python interpretation from an earlier behavior described in the standard Python documentation. " + \
                    "Removal of a feature also constitutes a change of behavior. This PEP does not replace or preclude other compatibility strategies such as dynamic loading of backwards-compatible parsers. On the other hand, if execution of old code requires a special switch or pragma then that is indeed a change of behavior from the point of view of the user and that change should be implemented according to these guidelines. "
obj_pep_text['6'] = "PEP 6 - Bug Fix Releases. Python has historically had only a single fork of development, with releases having the combined purpose of adding new features and delivering bug fixes (these kinds of releases will be referred to as major releases). This PEP describes how to fork off maintenance, or bug fix, releases of old versions for the primary purpose of fixing bugs. " + \
                    "This PEP is not, repeat NOT, a guarantee of the existence of bug fix releases; it only specifies a procedure to be followed if bug fix releases are desired by enough of the Python community willing to do the work. In general, common sense must prevail in the implementation of these guidelines. For instance changing sys.copyright does not constitute a backwards-incompatible change of behavior!"
obj_pep_text['7'] = "PEP 7 - Style Guide for C Code. This document gives coding conventions for the C code comprising the C implementation of Python. Please see the companion informational PEP describing style guidelines for Python code. Note, rules are there to be broken. Two good reasons to break a particular rule:" + \
                    "When applying the rule would make the code less readable, even for someone who is used to reading code that follows the rules. To be consistent with surrounding code that also breaks it (maybe for historic reasons) -- although this is also an opportunity to clean up someone else's mess (in true XP style)."
obj_pep_text['8'] = "PEP 8 - Style Guide for Python Code. This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. Please see the companion informational PEP describing style guidelines for the C code in the C implementation of Python. " + \
                    "This document and PEP 257 (Docstring Conventions) were adapted from Guido's original Python Style Guide essay, with some additions from Barry's style guide. This style guide evolves over time as additional conventions are identified and past conventions are rendered obsolete by changes in the language itself. " + \
                    "Many projects have their own coding style guidelines. In the event of any conflicts, such project-specific guides take precedence for that project."
obj_pep_text['10'] = "PEP 10 - Voting Guidelines. This PEP outlines the python-dev voting guidelines. These guidelines serve to provide feedback or gauge the wind direction on a particular proposal, idea, or feature. They don't have a binding force."
obj_pep_text['11'] = "PEP 11 - Removing support for little used platforms. This PEP documents how an operating system (platform) becomes supported in CPython and documents past support."
obj_pep_text['12'] = "This PEP provides a boilerplate or sample template for creating your own reStructuredText PEPs. In conjunction with the content guidelines in PEP 1, this should make it easy for you to conform your own PEPs to the format outlined below. " + \
                    "The source for this (or any) PEP can be found in the PEPs repository, viewable on the web at https://github.com/python/peps/"
obj_pep_text['512'] = "PEP 512 - Migrating from hg.python.org to GitHub. This PEP outlines the steps required to migrate Python's development process from Mercurial as hosted at hg.python.org to Git on GitHub. " + \
                    "Meeting the minimum goals of this PEP should allow for the development process of Python to be as productive as it currently is, and meeting its extended goals should improve the development process from its status quo."
obj_pep_text['20'] = "PEP 20 - The Zen of Python. Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. " + \
                    "Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. " + \
                    "In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. " + \
                    "Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"
obj_pep_text['101'] = "PEP 101 - Doing Python Releases 101. Making a Python release is a thrilling and crazy process.  You've heard the expression herding cats?  Imagine trying to also saddle those purring little creatures up, and ride them into town, with some of their " + \
                    "buddies firmly attached to your bare back, anchored by newly sharpened claws.  At least they're cute, you remind yourself. Actually, no that's a slight exaggeration.  The Python release process has steadily improved over the years and now, with the help of our amazing community, is really not too difficult. " + \
                    "This PEP attempts to collect, in one place, all the steps needed to make a Python release.  It is organized as a recipe and you can actually print this out and check items off as you complete them. "
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Pep Talk. " \
                    "You may ask me to read any of Python Enhancement " \
                    "Proposal eight, for example by saying, read me " \
                    "Pep eight."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Ask me to read you a pep. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying PepTalk. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def get_pep_text(pep_number):
    try:
        ret_text = obj_pep_text[pep_number]
    except KeyError as e:
        ret_text = "I don't know that pep."
    return ret_text


def get_pep(intent, session):
    """
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'pep' in intent['slots']:
        pep_number = intent['slots']['pep']['value']
        session_attributes = {'pep': pep_number}
        pep_text = get_pep_text(pep_number)
        speech_output = pep_text
        reprompt_text = "Ask about another pep if you want."
    else:
        speech_output = "I didn't recognise the request. " \
                        "Please try again."
        reprompt_text = "Ask me about another pep."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetPep":
        return get_pep(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
