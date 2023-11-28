// view_models/chat_screen_view_model.dart
import 'dart:async';

class ChatScreenViewModel {
  final List<String> _userMessages = [];
  final StreamController<List<String>> _messageController =
  StreamController<List<String>>.broadcast();

  Stream<List<String>> get messageStream => _messageController.stream;

  List<String> get userMessages => List.from(_userMessages);

  void dispose() {
    _messageController.close();
  }

  void sendMessage(String message) {
    _userMessages.add(message);
    _messageController.add(List.from(_userMessages));
  }
}

