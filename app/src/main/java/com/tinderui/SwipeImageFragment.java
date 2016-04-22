package com.tinderui;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import com.foodtinder.R;

/**
 * Created by pokeforce on 4/22/16.
 */
public class SwipeImageFragment extends Fragment {
    public static String INDEX = "Index";

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        int index = 0;
        if (getArguments() != null)
            index = getArguments().getInt(INDEX);

        View fragmentView = inflater.inflate(R.layout.fragment_slide_image, container, true);
        ImageView foodPicture = (ImageView) fragmentView.findViewById(R.id.imageview_tinder);

        if (index == 0) foodPicture.setImageResource(R.drawable.main_screen_no_checkers);
        else foodPicture.setImageResource(R.drawable.com_facebook_button_icon);
        
        return fragmentView;
    }
}
