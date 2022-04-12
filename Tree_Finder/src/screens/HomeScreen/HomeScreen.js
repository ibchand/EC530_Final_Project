import React, { useState, useEffect, Component } from "react";
import { View, Text } from "react-native";
import MapView, {PROVIDER_GOOGLE} from 'react-native-maps';
import styles from "./styles";

let firstCall = true;
let trees = require('../../../Trees.json'); 

export default function HomeScreen({ navigation }) {

  // const tree_data = require('')

  // const [trees, setTrees] = useState([{latitude: 42.3601,longitude: -71.0589}])

  // function firstCall() {
  //   if (firstCall) {
  //     let tree_data = require('../../../Trees.json'); 
  //     setTrees(tree_data);
  //     console.log("Bruh")
  //   }
  //   firstCall = false;
  // }

  // firstCall();

  return (
    <View style={styles.container}>
        <Text>Home Screen</Text>
        <MapView 
          provider={PROVIDER_GOOGLE}
          style={styles.map}
          region={{
              latitude: 42.3601,
              longitude: -71.0589,
              latitudeDelta: 0.1,
              longitudeDelta: 0.1
          }}
        >
          {
            trees.map((element, index) => {
              return (
                <MapView.Marker
                  key={index}
                  coordinate={{ latitude: element["long"], longitude: element["lat"] }}
                  title={"fjsdkalfjklasdfj"}
                  description={"jflkdasjfklsadjfklsajflksdajf"}
                />
              );
            })
          }
        </MapView>
    </View>
  );
}
