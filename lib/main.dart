import 'dart:developer';
import 'package:http/http.dart' as http;
import 'dart:convert' as convert;
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'dart:async';
import 'package:material_floating_search_bar/material_floating_search_bar.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  // This widget is the root of your application.
  @override
  State<StatefulWidget> createState (){
    return MyHomePage();
  }
}

class MyHomePage extends State<MyApp>{

  var batPer;
  var progPer;

  @override
  void initState() {
    super.initState();
  }

  @override
  Widget build(BuildContext context) {

    return MaterialApp(
      home: Scaffold(
        extendBodyBehindAppBar: true,
      drawer: Theme(
        data: Theme.of(context).copyWith(
      // Set the transparency here
          canvasColor: Colors.transparent, //or any other color you want. e.g Colors.blue.withOpacity(0.5)
        ),
        child: Drawer(
          child: ListView(
            children: <Widget>[
              Card(
                color: Colors.grey[300],
                child: ListTile(
                  leading: Icon(Icons.home, color: Colors.black, size: 50.0),
                  title: Text('Home',style: TextStyle(fontSize: 40)),

                  onTap: () {
                    Navigator.pop(context);
                  },
                ),
              ),
              Card(
                color: Colors.grey[300],
                child: ListTile(
                  leading: Icon(Icons.map, color: Colors.black, size: 50.0),
                  title: Text('Map',style: TextStyle(color: Colors.black, fontSize: 40)),
                  onTap: () {
                    Navigator.of(context).push(new MaterialPageRoute(builder:
                        (BuildContext context) => new MyMapPage()));
                  },
                ),
              ),
              Card(
                color: Colors.grey[300],
                child: ListTile(
                  leading: Icon(Icons.cloud, color: Colors.black, size: 50.0),
                  title: Text('Weather',style: TextStyle(fontSize: 40)),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => MyWeatherPage()),
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),

      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text('Home'),
        backgroundColor: Colors.transparent,
      ),
      body: Stack(
        children:[
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
          Image.asset(
            'images/lawn.jpg',
            fit: BoxFit.cover,
            height: double.infinity,
            width: double.infinity,
          ),
          Container(
            decoration: BoxDecoration(color: Colors.white24),
          ),
          Container(
          width: double.infinity,
          height: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
            Container(
              width: 200.0,
              height: 200.0,
              child: ElevatedButton(
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(Colors.green.withOpacity(0.3)),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(100.0),
                      side: BorderSide(color: Colors.black)
                    ),
                  ),
                ),
                child: Icon(
                  Icons.power_settings_new_rounded,
                  size: 150,
                ),
                onPressed: (){},
              ),
            ),
            Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Expanded(
                    child: Column(
                      children: [
                        Icon(Icons.battery_full_outlined, size: 200.0, color: Colors.grey),
                        Text('$batPer %', style: TextStyle(fontSize: 30.0),)
                      ],
                    ),
                  ),
                  Expanded(
                    child: Column(
                      children: [
                        Icon(Icons.wine_bar_sharp, size: 200.0, color: Colors.grey),
                        Text('$progPer %', style: TextStyle(fontSize: 30.0))
                      ],
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
        ],
      ),
    ),
    );
  }
}

class MyMapPage extends State<MyApp> {

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return MaterialApp(
      home: Scaffold(
      extendBodyBehindAppBar: true,
 /*     drawer: Theme(
        data: Theme.of(context).copyWith(
      // Set the transparency here
          canvasColor: Colors.transparent, //or any other color you want. e.g Colors.blue.withOpacity(0.5)
        ),
        child: Drawer(
          child: ListView(
            children: <Widget>[
              Card(
                color: Colors.grey[300],
                child: ListTile(
                  leading: Icon(Icons.home, color: Colors.black, size: 50.0),
                  title: Text('Home',style: TextStyle(fontSize: 40)),

                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => MyHomePage()),
                    );
                  },
                ),
              ),
              Card(
                color: Colors.grey[300],
                child: ListTile(
                  leading: Icon(Icons.map, color: Colors.black, size: 50.0),
                  title: Text('Map',style: TextStyle(color: Colors.black, fontSize: 40)),
                  onTap: () {
                    Navigator.pop(context);
                  },
                ),
              ),
              Card(
                color: Colors.grey[300],
                child: ListTile(
                  leading: Icon(Icons.cloud, color: Colors.black, size: 50.0),
                  title: Text('Weather',style: TextStyle(fontSize: 40)),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => MyWeatherPage()),
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),*/
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text('Map'),
        backgroundColor: Colors.transparent,
      ),
      body: Stack(
        children:[
          Image.asset(
            'images/night.jpg',
            fit: BoxFit.cover,
            height: double.infinity,
            width: double.infinity,
          ),
          Container(
            decoration: BoxDecoration(color: Colors.black38),
          ),
          Container(
          width: double.infinity,
          height: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Container(
                height: 400,
                width: 300,
                decoration: BoxDecoration(
                  color: Colors.grey,
                    border: Border.all(
                    ),
                    borderRadius: BorderRadius.all(Radius.circular(20))
                ),
                child: Center(child: Text('Map')),
              ),
              Container(
                width: 200.0,
                height: 70.0,
                child: ElevatedButton(
                    style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all<Color>(Colors.green),
                        shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                            RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(18.0),
                                side: BorderSide(color: Colors.black)
                            ),
                        ),
                    ),
                  child: Row(
                    children: [
                      Icon(Icons.adjust, size: 40.0),
                      SizedBox(width: 20.0),
                      Text('Locate', style: TextStyle(fontSize: 30.0)),
                    ],
                  ),
                  onPressed: (){},
                ),
              ),
            ],
          ),
        ),
        ],
      ),
      ),
    );
  }
}

class MyWeatherPage extends State<MyApp> {

  Timer timer;
  DateTime nowDate = new DateTime.now();
  var temp;
  var description;
  var currently;
  var humidity;
  var windSpeed;
  var location;


  Future getWeather () async{
    http.Response response = await http.get(Uri.parse("https://api.openweathermap.org/data/2.5/weather?q=Zurich&appid=dca18836b898915425dcb7e463fb9724"));
    var results = convert.jsonDecode(response.body);
    setState(() {
      this.temp = results['main']['temp'];
      this.description = results['weather'][0]['main'];
      this.currently = results['weather'][0]['main'];
      this.humidity = results['main']['humidity'];
      this.windSpeed = results['wind']['speed'];

    });
  }
/*
  Future updateBackdrop () async{
    setState(() {
      switch (description){
        case 'Rain':
          backdrop = 'images/rain.jpg';
          break;
        case 'Clear':
          backdrop = 'images/sunny.jpg';
          break;
        case 'Clouds':
          backdrop = 'images/cloudy.jpeg';
          break;
      }
    });
  }
*/
  @override
  void initState() {
    super.initState();
    this.getWeather();
    timer = Timer.periodic(Duration(seconds: 1), (Timer t) => getWeather());
 //   this.updateBackdrop();
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return MaterialApp(
      home: Scaffold(
        extendBodyBehindAppBar: true,
   /*   drawer: Theme(
          data: Theme.of(context).copyWith(
        // Set the transparency here
          canvasColor: Colors.transparent, //or any other color you want. e.g Colors.blue.withOpacity(0.5)
          ),
          child: Drawer(

              child: ListView(

                children: <Widget>[
                  Card(
                    color: Colors.grey[300],
                    child: ListTile(
                      leading: Icon(Icons.home, color: Colors.black, size: 50.0),
                      title: Text('Home',style: TextStyle(fontSize: 40)),

                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => MyHomePage()),
                        );
                      },
                    ),
                  ),
                  Card(
                    color: Colors.grey[300],
                    child: ListTile(
                      leading: Icon(Icons.map, color: Colors.black, size: 50.0),
                      title: Text('Map',style: TextStyle(color: Colors.black, fontSize: 40)),
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => MyMapPage()),
                        );
                      },
                    ),
                  ),
                  Card(
                    color: Colors.grey[300],
                    child: ListTile(
                      leading: Icon(Icons.cloud, color: Colors.black, size: 50.0),
                      title: Text('Weather',style: TextStyle(fontSize: 40)),
                      onTap: () {
                        Navigator.pop(context);
                      },
                    ),
                  ),
                ],
              ),
            ),
          ),*/
        appBar: AppBar(
          // Here we take the value from the MyHomePage object that was created by
          // the App.build method, and use it to set our appbar title.
          title: Text('Weather'),
          backgroundColor: Colors.transparent,
        ),
        body: Center(
          // Center is a layout widget. It takes a single child and positions it
          // in the middle of the parent.
          child: Stack(
            children: [
              Image.asset(
                'images/night.jpg',
                fit: BoxFit.cover,
                height: double.infinity,
                width: double.infinity,
              ),
              Container(
                decoration: BoxDecoration(color: Colors.black38),
              ),
              Container(
                padding: EdgeInsets.all(20),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Expanded(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              SizedBox(height: 100,),
                              Text(
                                'Zürich',
                                style: TextStyle(
                                  fontSize: 45.0,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              ),
                              Text(
                                '${nowDate.hour}:${nowDate.minute}  - ${nowDate.day}.${nowDate.month}.${nowDate.year}',
                                style: TextStyle(
                                  fontSize: 15.0,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              ),
                            ],
                          ),
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                '${(temp-273.15).toStringAsFixed(0)}\u2103',
                                style: TextStyle(
                                  fontSize: 100.0,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.white,
                                ),
                              ),
                              Row(
                                children: [
                                  Text(
                                    '$description',
                                    style: TextStyle(
                                      fontSize: 15.0,
                                      fontWeight: FontWeight.bold,
                                      color: Colors.white,
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                    Column(
                      children: [
                        Container(
                          margin: EdgeInsets.symmetric(vertical: 40),
                          decoration: BoxDecoration(
                            border: Border.all(
                              color: Colors.white30,
                            ),
                          ),
                        ),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                          children: [
                            Column(
                              children: [
                                Text(
                                  'Wind',
                                  style: TextStyle(
                                    fontSize: 15.0,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.white,
                                  ),
                                ),
                                Text(
                                  '$windSpeed m/h',
                                  style: TextStyle(
                                    fontSize: 35.0,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.white,
                                  ),
                                ),
                              ],
                            ),

                            Column(
                              children: [
                                Text(
                                  'Humidity',
                                  style: TextStyle(
                                    fontSize: 15.0,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.white,
                                  ),
                                ),
                                Text(
                                  '$humidity\u0025',
                                  style: TextStyle(
                                    fontSize: 35.0,
                                    fontWeight: FontWeight.bold,
                                    color: Colors.white,
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                      ],
                    ),

                  ],
                ),

              ),
            ],
          ),
        ),
      ),
    );
  }
}
