// view_models/chat_screen_view_model.dart
import 'dart:async';
import 'package:http/http.dart' as http;

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
    _sendMessageToServer(message);
    _messageController.add(List.from(_userMessages));

    // Send the message to the server
    _sendMessageToServer(message);
  }

  Future<void> _sendMessageToServer(String message) async {
    const String getUrl = 'http://localhost:8000/llm/'; // Replace with your actual API endpoint for GET request

    try {
      // Send a GET request
      final getResponse = await http.get(Uri.parse(getUrl));

      if (getResponse.statusCode == 200) {
        print('GET request successful. Response: ${getResponse.body}');
      } else {
        print('Failed to make GET request. Status code: ${getResponse.statusCode}');
      }
    } catch (e) {
      print('Error: $e');
    }
  }
}



