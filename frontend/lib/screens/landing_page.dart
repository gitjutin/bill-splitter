import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

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
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  const SizedBox(height: 75),
                  Center(
                    child: Text(
                      'Itemized',
                      style: GoogleFonts.playfair(
                        fontSize: 65,
                        //fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                  ),
                  
                  const Spacer(),

                  FilledButton(
                      onPressed: (){
                        // TODO: add navigation logic
                      },
                      style: FilledButton.styleFrom(
                        //backgroundColor: Colors.transparent,
                        backgroundColor: Colors.white.withValues(alpha: 0.15),
                        //foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 12),
                      ),
                      child: Text(
                        'New Bill',
                        style: GoogleFonts.playfair(
                          fontSize: 35,
                          color: Colors.white,
                        ),
                      ),
                  ),
                ],
              ),
            ),
          ),
        ]),
    );
  }
}
