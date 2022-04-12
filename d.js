import React, { useState, useEffect, Component } from "react";
import { View, Text } from "react-native";
import { MapView, Marker } from 'react-native-maps';
import styles from "./styles";

export default function HomeScreen({ navigation }) {

  const trees = [
    {
      "lat": -71.0576630211364,
      "long": 42.3548674801392
    },
    {
      "lat": -71.0577011371316,
      "long": 42.3548780872298
    },
    {
      "lat": -71.0577967217474,
      "long": 42.3547845778359
    },
    {
      "lat": -71.0562927334319,
      "long": 42.3547404512128
    },
    {
      "lat": -71.0563076884897,
      "long": 42.3548220087004
    },
    {
      "lat": -71.056277751873,
      "long": 42.3546580050316
    },
    {
      "lat": -71.0565033119221,
      "long": 42.3539616902509
    },
    {
      "lat": -71.0565716806008,
      "long": 42.3539531328432
    }
  ]


  return (
    <View style={styles.container}>
      <Text>Home Screen</Text>
        <MapView 
          style={styles.map}
          region={{
            latitude: 42.3601,
            longitude: -71.0589,
            latitudeDelta: 0.1,
            longitudeDelta: 0.3
          }}
        >
        <Marker
          key={1}
          coordinate={{ latitude: 42.3601, longitude: -71.0589 }}
          // title={marker.title}
          // description={marker.description}
        />
      </MapView>
    </View>
  );
}
