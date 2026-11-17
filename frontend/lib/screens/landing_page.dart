import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart'

class LandingPage extends StatelessWidget {
  const LandingPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset(
            'assets/images/blurredBG.png',
            fit: BoxFit.cover,
          ),

          Container(color: Colors.black.withValues(alpha: 0.4)),

          SafeArea(
            child: Padding(
              padding: const EdgeInsetsGeometry.all(24),
              child: Column(
                children: [
                  const SizedBox(height: 50),
                  const Text(
                    'Itemized',
                    style: TextStyle(
                      fontSize: 50,
                      //fontWeight: FontWeight.bold,
                      color: Colors.white,
                    )
                  )
                ],
              ),
            ),
          ),
        ]),
    );
  }
}
