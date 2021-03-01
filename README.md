# Object Oriented Programming @MAU - FM V.2
A Python project made with an intend to handle object oriented programming through creating new participants by using classes following the UML diagram.
<br> <br> I chose to model a Football Manager knockoff game, which contains a football league (League) with football teams (Team), which all have 0-* players (Player) and 0-1 coach (Coach).

![OOP-INL](https://user-images.githubusercontent.com/40041318/109473470-9b48cf80-7a73-11eb-9d26-45a3d10ec8b4.jpg)


One could argue that the UML could be misleading, though the League class can exist without the Football_Manager class and therefore also should have an aggregation connection between the two. However, I chose to go with composition since the League object is created in the Football_Manager constructor and then cannot exist without the Football_Manager class doing so.

<ul>
  <legend><b>How to use the application</b></legend>
  <li>Python V3.8 or later installed</li>
  <li>Open the project in your prefered texteditor</li>
  <li>Navigate to the fotball_manager.py file</li>
  <li>Run the file</li>
  <li>Folow the instructions presented</li>
</ul>
