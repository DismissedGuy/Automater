# Intro
People are lazy. We enjoy making others do the tough or long-winded work for us. That's why we invented robots that do all kinds of stuff for us. But not everyone has implemented these robots yet. What if I told you that there's a way to automate your Discord server? Wouldn't that be amazing?

## Introducing Automater
Well, as it turns out, there is a way! Originally created as a submission for Discord's Hack Week 2019, this bot allows you to automate every aspect of your server.* And that with no prior programming knowledge! No messing around with stupid configs, every server admin can automate their server using a simple web form. No more inviting all sorts of bots to support just that feature that you like most. With automater, _you_ are in control. Create your own unique features from scratch. I'm telling you, it's great. Absolutely a-ma-zing. Let's make Discord great again.

*Not all functions might be implemented, but relatively easy to support using config files.

## Breakdown
That's cool and all, but how do I use it? Simple! When you invite the bot, you can invoke the `.setup` command and the bot will show you a link to set up your first macro. Simply fill out the form, accept to the oauth request and your macro will be installed!
The usage of these "macros" is also quite easy to understand... to show you, I have made this awesome markdown header tree. Check it out:

### Macro
This is how you call a combination of events, conditions, actions and arguments. Be not afraid, you fool; more on these terms below.

#### Events
Events are simply things that happen on your discord server. For example, MESSAGE_CREATE is an event that triggers when you send a message.

#### Conditions
Conditions are statements that regulate and control when events are called. For example, you might only want to execute an action on your server when a message contains the word "wumpus."

#### Actions
A simple term to describe... an action. For example, you might want the bot to change someone's nickname, or create a channel.

#### Arguments
Actions are great and all, but how would the bot know which channel to create? Or what should the name be? This is where arguments (or simply args) come into action. the argument "channel_name" might describe the name of a new channel to create, for example.

## Screenshots
Because human beings like por.. uh.. visual imagery.