// views/app_view.dart
import 'package:flutter/material.dart';
import 'chat_screen_view.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        brightness: Brightness.dark,
        primaryColor: Colors.green,
      ),
      home: const ChatScreen(),
    );
  }
}
