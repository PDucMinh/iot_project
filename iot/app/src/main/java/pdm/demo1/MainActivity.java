package pdm.demo1;

import androidx.appcompat.app.AppCompatActivity;
//import MQTTHelper;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class MainActivity extends AppCompatActivity {
    MQTTHelper mqtthelper;
    TextView txtTemp, txtHumi;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtTemp = findViewById(R.id.txtTempurature);
        txtHumi = findViewById(R.id.txtHumidity);

        startMQTT();
    }
    public void startMQTT(){
        mqtthelper = new MQTTHelper(this);
        mqtthelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("TEST", topic + " -lmao- " +message.toString());
                if (topic.contains("sensor1")){
                    txtTemp.setText(message.toString() + " °C");
                }
                else if (topic.contains("sensor2")){
                    txtHumi.setText(message.toString() + " °C");
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}